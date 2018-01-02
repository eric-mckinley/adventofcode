class ParticleData:
    def __init__(self, id, info):
        self.id = id

        datalist = info.split(">")
        pos = datalist[0].replace(" ", "")
        vel = datalist[1].replace(" ", "")
        acc = datalist[2].replace(" ", "")
        self.position = VectorData(pos[pos.index("<") +1:])
        self.velocity = VectorData(vel[vel.index("<") +1:])
        self.acceleration = VectorData(acc[acc.index("<") +1:])

    def __str__(self):
        return "Particle: pos: [{}], vel: [{}], acc:[{}]".format(self.position, self.velocity, self.acceleration)

    def tick(self):
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    def manDist(self):
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

class VectorData:
    def __init__(self, info):

        numlist = info.split(",")
        self.x = int(numlist[0])
        self.y = int(numlist[1])
        self.z = int(numlist[2])

    def __str__(self):
        return "VectorData: x: [{}], y: [{}], z:[{}]".format(self.x, self.y, self.z)

def runProgram(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    pid =0
    particles = list()
    for line in lines:
        particles.append(ParticleData(pid, line))
        pid += 1

    for i in range(0, 15000):
        print("Tick {}".format(i))
        for particle in particles:
            particle.tick()

    closest = particles[0]
    for particle in particles:
        print(particle.manDist())
        if particle.manDist() < closest.manDist(): closest = particle

    print("Particle {} is closest with distance: {}".format(closest.id, closest.manDist()))
# runProgram("sample.txt")
runProgram("input.txt")