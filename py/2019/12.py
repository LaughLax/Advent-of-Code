import numpy as np
import matplotlib.pyplot as plt


class AdventOfCode:

    def __init__(self, filename):
        with open(filename) as f:
            self.input = eval(f.read().strip())
        self.moons_pos_i = np.array(self.input, dtype=np.int16)
        '''
        self.moons_pos_i = np.array([[-1, 0, 2],  # Example 1
                                   [2, -10, -7],
                                   [4, -8, 8],
                                   [3, 5, -1]])
        self.moons_pos_i = np.array([[-8, -10, 0],  # Example 2
                                   [5, 5, 10],
                                   [2, -7, 3],
                                   [9, -8, -3]])
        '''
        self.moons_vel_i = np.zeros((4,3), dtype=np.int16)

    def part1(self):
        adj = np.array([[1, -1, 0, 0],
                        [1, 0, -1, 0],
                        [1, 0, 0, -1],
                        [0, 1, -1, 0],
                        [0, 1, 0, -1],
                        [0, 0, 1, -1]])

        step = 0
        moons_pos = self.moons_pos_i.copy()
        moons_vel = self.moons_vel_i.copy()
        while step < 1000:
            vel_change = -adj.T.dot(np.sign(adj.dot(moons_pos)))
            moons_vel += vel_change
            moons_pos += moons_vel
            step += 1

        tot_energy = 0
        for a in range(4):
            energy = np.sum(np.abs(moons_pos[a])) * np.sum(np.abs(moons_vel[a]))
            tot_energy += energy

        return tot_energy

    def part2(self):
        adj = np.array([[1, -1, 0, 0],
                        [1, 0, -1, 0],
                        [1, 0, 0, -1],
                        [0, 1, -1, 0],
                        [0, 1, 0, -1],
                        [0, 0, 1, -1]])

        step = 0

        moons_pos = self.moons_pos_i.copy()
        moons_vel = self.moons_vel_i.copy()

        hash_vx = hash(bytes(moons_vel[:, 0]))
        hash_vy = hash(bytes(moons_vel[:, 1]))
        hash_vz = hash(bytes(moons_vel[:, 2]))

        # Leaving some scrapped work product in here because it makes for nice visuals

        # length = 64000
        # pos = np.zeros((length + 1, 12))
        # vel = np.zeros((length + 1, 12))
        # pos[0] = moons_pos.flatten()
        # vel[0] = moons_vel.flatten()

        x_rep = None
        y_rep = None
        z_rep = None

        while x_rep is None or y_rep is None or z_rep is None:
            vel_change = -adj.T.dot(np.sign(adj.dot(moons_pos)))
            moons_vel += vel_change
            moons_pos += moons_vel
            step += 1

            # pos[step] = moons_pos.flatten()
            # vel[step] = moons_vel.flatten()

            # Assumed and hoped that the loop begins at t=0. Turns out that assumption was good!
            # There used to be code for storing historical states. It's gone now.
            if x_rep is None and \
                    hash(bytes(moons_vel[:, 0])) == hash_vx and \
                    np.array_equal(moons_vel[:, 0], self.moons_vel_i[:, 0]):
                x_rep = step
            if y_rep is None and \
                    hash(bytes(moons_vel[:, 1])) == hash_vy and \
                    np.array_equal(moons_vel[:, 1], self.moons_vel_i[:, 1]):
                y_rep = step
            if z_rep is None and \
                    hash(bytes(moons_vel[:, 2])) == hash_vz and \
                    np.array_equal(moons_vel[:, 2], self.moons_vel_i[:, 2]):
                z_rep = step

            # if step == length:
            #     break

        # x = range(length + 1)

        # fig, axes = plt.subplots(nrows=12, ncols=1)
        # for a in range(12):
        #     axes[a].plot(x, pos[:, a])

        # fig, axes = plt.subplots(nrows=12, ncols=1)
        # for a in range(12):
        #     axes[a].plot(x, vel[:, a])
        
        # fig, axes = plt.subplots(nrows=8, ncols=1)
        # axes[0].plot(x, pos[:, 0], '-b', linewidth=1)
        # axes[1].plot(x, pos[:, 3], '-b', linewidth=1)
        # axes[2].plot(x, pos[:, 6], '-b', linewidth=1)
        # axes[3].plot(x, pos[:, 9], '-b', linewidth=1)
        # axes[4].plot(x, vel[:, 0], '-r', linewidth=1)
        # axes[5].plot(x, vel[:, 3], '-r', linewidth=1)
        # axes[6].plot(x, vel[:, 6], '-r', linewidth=1)
        # axes[7].plot(x, vel[:, 9], '-r', linewidth=1)

        # for ax in axes:
        #     ax.set_xlim(0, length+1)

        # plt.tight_layout()
        # plt.show()

        return np.lcm(np.lcm(x_rep, y_rep, dtype=np.int64), z_rep, dtype=np.int64) * 2

