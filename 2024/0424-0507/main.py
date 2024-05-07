from persor import BVHparser
from scipy.spatial.transform import Rotation
import matplotlib.pyplot as plt
import numpy as np
import copy
import japanize_matplotlib


def get_joint_coords(skeleton, joint, coords):
    offset = skeleton[joint]["offset"]
    parent_joint = skeleton[joint]["joint"]
    child_joints = skeleton[joint]["children"]

    if parent_joint == None:
        return

    parent_coord = coords[parent_joint]["coord"]

    current_coord = [
        parent_coord[0] + offset[0],
        parent_coord[1] + offset[1],
        parent_coord[2] + offset[2],
    ]
    coords[joint] = {"coord": current_coord, "parent": parent_joint}

    for child in child_joints:
        get_joint_coords(skeleton, child, coords)


def skelton2coords(skeleton):
    coords = {"root": {"coord": skeleton["root"]["offset"], "parent": None}}
    skeleton["root"]

    child_joints = skeleton["root"]["children"]
    for child in child_joints:
        get_joint_coords(skeleton, child, coords)

    get_joint_coords(skeleton, "root", coords)

    return coords


def rotated_offset(skeleton, frame):
    skeleton_copy = copy.deepcopy(skeleton)
    for joint, data in skeleton_copy.items():
        if joint == "root" or joint.startswith("_"):
            continue

        x_rotate = np.deg2rad(frame[f"{joint}_Xrotation"])
        y_rotate = np.deg2rad(frame[f"{joint}_Yrotation"])
        z_rotate = np.deg2rad(frame[f"{joint}_Zrotation"])

        rot = Rotation.from_rotvec(np.array([z_rotate, y_rotate, x_rotate]))
        skeleton_copy[joint]["offset"] = rot.apply(data["offset"])

    return skeleton_copy


def plot_skeleton(coords, title="骨格"):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    for joint, coord in coords.items():
        if coord["parent"] == None:
            continue
        parent_coord = coords[coord["parent"]]["coord"]
        ax.plot(
            [parent_coord[0], coord["coord"][0]],
            [parent_coord[2], coord["coord"][2]],
            [parent_coord[1], coord["coord"][1]],
            marker="o",
        )
    plt.title(title)
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.ylabel("z[m]")
    ax.set_xlim(-90, 90)
    ax.set_ylim(-90, 90)
    ax.set_zlim(0, 190)

    plt.show()


bvhp = BVHparser("./data/jump.bvh")
skeleton = bvhp.get_skeleton()
motion_df = bvhp.get_motion_df()

for i in range(0, 500, 50):
    motion_frame = motion_df.iloc[i, :]
    rotated_skeleton = rotated_offset(skeleton, motion_frame)
    rotated_coord = skelton2coords(rotated_skeleton)
    plot_skeleton(rotated_coord, f"回転後の骨格({i}フレーム)")

motion_frame = motion_df.iloc[200, :]

rotated_skeleton = rotated_offset(skeleton, motion_frame)
rotated_coord = skelton2coords(rotated_skeleton)
plot_skeleton(rotated_coord, "回転後の骨格")
