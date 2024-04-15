using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class posture : MonoBehaviour
{
    // Start is called before the first frame update
    // ゲームオブジェクトを入れる
    public GameObject obj;

    void Start()
    {
        // CSVファイルのパスを設定する
        string filePath = Application.dataPath + "/posture.csv";

        // CSVファイルを開く
        StreamReader reader = new StreamReader(filePath);

        // データを読み込む
        List<Vector3> rotateList = new List<Vector3>();
        List<float> yList = new List<float>();
        while (!reader.EndOfStream)
        {
            string[] line = reader.ReadLine().Split(',');
            float time = float.Parse(line[0], System.Globalization.NumberStyles.Float);
            float pitch = float.Parse(line[1], System.Globalization.NumberStyles.Float);
            float roll = float.Parse(line[2], System.Globalization.NumberStyles.Float);
            float yaw = float.Parse(line[3], System.Globalization.NumberStyles.Float);
            float y = float.Parse(line[4], System.Globalization.NumberStyles.Float);
            
            rotateList.Add(new Vector3(pitch, roll, yaw));
            yList.Add(y);
        }

        // ファイルを閉じる
        reader.Close();
    }

    // Update is called once per frame
    void Update()
    {
        timer += Time.deltaTime * 4;
        if (timer >= 1f) {
            currentIndex++;
            if (currentIndex >= rotateList.Count) currentIndex = 0;

            transform.rotation = Quaternion.Euler(rotateList[currentIndex]);
            transform.position.y = yList[currentIndex];
            timer = 0;
        }
    }
}
