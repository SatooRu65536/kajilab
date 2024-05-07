from persor import BVHparser

def get_joint_coords(skeleton, joint, frame, coords):
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
    coords[joint] = { "coord": current_coord, "parent": parent_joint }

    for child in child_joints:
        get_joint_coords(skeleton, child, frame, coords)


def skelton2coords(skeleton, frame):
    coords = {"root": { "coord": [0, 0, 0], "parent": None }}
    skeleton["root"]

    child_joints = skeleton["root"]["children"]
    for child in child_joints:
        get_joint_coords(skeleton, child, frame, coords)

    get_joint_coords(skeleton, "root", frame, coords)

    return coords

bvhp = BVHparser("./data/jump.bvh")
skeleton = bvhp.get_skeleton()
motion_df = bvhp.get_motion_df()
motion_frame = motion_df.iloc[100,:]
coords = skelton2coords(skeleton, motion_frame)
print(coords)

import matplotlib.pyplot as plt
import japanize_matplotlib

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
for joint, coord in coords.items():
    if coord["parent"] == None:
        continue
    parent_coord = coords[coord["parent"]]["coord"]
    ax.plot(
        [parent_coord[0], coord["coord"][0]],
        [parent_coord[1], coord["coord"][1]],
        [parent_coord[2], coord["coord"][2]],
        marker="o",
    )

plt.title('骨格')
plt.xlabel('x[m]')
plt.ylabel('y[m]')
plt.ylabel('z[m]')

plt.show()

