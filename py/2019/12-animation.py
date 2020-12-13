from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm


with open(r'.\input\2019-12.txt') as f:
    my_input = eval(f.read().strip())
moons_pos_i = np.array(my_input, dtype=np.int16)
moons_vel_i = np.zeros((4,3), dtype=np.int16)

adj = np.array([[1, -1, 0, 0],
                [1, 0, -1, 0],
                [1, 0, 0, -1],
                [0, 1, -1, 0],
                [0, 1, 0, -1],
                [0, 0, 1, -1]])

step = 0

moons_pos = moons_pos_i.astype(np.float32)
moons_vel = moons_vel_i.astype(np.float32)

length = 1000
pos = np.zeros((length + 1, 12))
vel = np.zeros((length + 1, 12))
pos[0] = moons_pos.flatten()
vel[0] = moons_vel.flatten()

while step < length / 10:
    moons_vel += -adj.T.dot(np.sign(adj.dot(moons_pos)))

    for i in range(10):
        vel[step*10 + i + 1] = moons_vel.flatten()
        pos[step*10 + i + 1] = moons_pos.flatten() + i * moons_vel.flatten() / 10.

    step += 1
    moons_pos += moons_vel

t = range(length + 1)

x_pos = pos[:,[0, 3, 6, 9]]
y_pos = pos[:,[1, 4, 7, 10]]
z_pos = pos[:,[2, 5, 8, 11]]

ax = plt.axes(projection='3d')
lines = []
for i in range(4):
    lines.extend(ax.plot3D(x_pos[:, i], y_pos[:, i], z_pos[:, i], ':'))
dots = ax.plot(x_pos[-1, :], y_pos[-1, :], z_pos[-1, :], linestyle='', marker='o')[0]

plt.tight_layout()

def interpolate(i):
    pass

def animate(i):
    pbar.update(1)
    ax.view_init(30, i/10. % 360)

    start = max(i-99, 0)
    for p in range(4):
        lines[p].set_data_3d(x_pos[start:i+1, p], y_pos[start:i+1, p], z_pos[start:i+1, p])
    dots.set_data(x_pos[i, :], y_pos[i, :])
    dots.set_3d_properties(z_pos[i, :])

    artists = [ax] + lines + [dots]
    # artists.extend(lines)
    # artists.append(dots)

    return artists

fig = plt.gcf()
ani = animation.FuncAnimation(fig, animate, frames=length, blit=False, repeat_delay=10)

FPS = 60
SAMPLE_RATE = 10

plt.rcParams['animation.ffmpeg_path'] = r'C:\OSGeo4W64\bin\ffmpeg.exe'
FFwriter = animation.FFMpegWriter(fps=FPS)
vid_len = length/FPS
vid_speed = FPS/SAMPLE_RATE
print(f'Video will be {vid_len:.2f} seconds long playing at {vid_speed:3.1f}x speed.')

pbar = tqdm(total=length+1)
ani.save('2019-12-orbits-rotating.mp4', writer=FFwriter)
pbar.close()

# plt.show()
plt.close()

# fig, axes = plt.subplots(nrows=12, ncols=1)
# for a in range(12):
#     axes[a].plot(t, pos[:, a])

# fig, axes = plt.subplots(nrows=12, ncols=1)
# for a in range(12):
#     axes[a].plot(t, vel[:, a])
        
# fig, axes = plt.subplots(nrows=8, ncols=1)
# axes[0].plot(t, pos[:, 0], '-b', linewidth=1)
# axes[1].plot(t, pos[:, 3], '-b', linewidth=1)
# axes[2].plot(t, pos[:, 6], '-b', linewidth=1)
# axes[3].plot(t, pos[:, 9], '-b', linewidth=1)
# axes[4].plot(t, vel[:, 0], '-r', linewidth=1)
# axes[5].plot(t, vel[:, 3], '-r', linewidth=1)
# axes[6].plot(t, vel[:, 6], '-r', linewidth=1)
# axes[7].plot(t, vel[:, 9], '-r', linewidth=1)

# for ax in axes:
#     ax.set_xlim(0, length+1)

# plt.tight_layout()
# plt.show()
