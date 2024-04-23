import cv2
import numpy as np
import mediapipe as mp

# 今回使うグラフのセッティング
num_node = 17
E = [[15,13],[13,11],[16,14],[14,12],[11,12],[5,11],
     [6,12],[5,6],[5,7], [6,8],[7,9],[8,10],[1,2],
     [0,1],[0,2],[1,3],[2,4],[3,5],[4,6]]
reduced_keypoints = [0,2,5,7,8,11,12,13,14,15,16,23,24,25,26,27,28] # 関節数が多すぎてごちゃつくので必要な分だけピックアップ

# APIで推定した座標をnumpy配列に変換
def make_spatial_feature_mx(hand_landmarks, width, height):
    spatial_mx = []
    for i, lm in enumerate(hand_landmarks.landmark):
        if i in reduced_keypoints:
            x = lm.x * width
            y = lm.y * height
            spatial_mx.append([x, y])
    spatial_mx = np.array(spatial_mx)
    return spatial_mx   # shape (V, C)
    
# videoの読み込み
cap = cv2.VideoCapture("asset/spatial-temporal-graph-convolutional-network/video.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

X = []
#pose推定の設定
mp_pose = mp.solutions.pose
with mp_pose.Pose(
    min_detection_confidence=0.5,   
    min_tracking_confidence=0.5) as pose:
    
    idx = 0
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, idx * fps) # 動きがわかりやすいように1秒ごと取得
        success, image = cap.read()
        if not success:
            break

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        
        X_t = make_spatial_feature_mx(results.pose_landmarks, width, height)    # 各フレームでの特徴行列を作成
        X.append(X_t)   # 時間方向に追加する
        idx += 1
        
X = np.array(X)
X.shape # T V C
