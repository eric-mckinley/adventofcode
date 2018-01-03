class ParticleData:
    def __init__(self, id, info):
        self.id = id
        self.eliminated = False
        datalist = info.split(">")
        pos = datalist[0].replace(" ", "")
        vel = datalist[1].replace(" ", "")
        acc = datalist[2].replace(" ", "")
        self.position = VectorData(pos[pos.index("<") + 1:])
        self.velocity = VectorData(vel[vel.index("<") + 1:])
        self.acceleration = VectorData(acc[acc.index("<") + 1:])
        self.distance = abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    def shareSamePosition(self, other):
        return self.position.x == other.position.x and self.position.y == other.position.y and self.position.z == other.position.z

    def __str__(self):
        return "Particle: pos: [{}], vel: [{}], acc:[{}]".format(self.position, self.velocity, self.acceleration)

    def tick(self):
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z
        self.distance = abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

class VectorData:
    def __init__(self, info):
        numlist = info.split(",")
        self.x = int(numlist[0])
        self.y = int(numlist[1])
        self.z = int(numlist[2])

    def __str__(self):
        return "VectorData: x: [{}], y: [{}], z:[{}]".format(self.x, self.y, self.z)

def notEliminated(element):
    return element.eliminated == False

def loadParticles(inputfile):
    with open(inputfile) as f:
        lines = f.readlines()

    pid = 0
    particles = list()
    for line in lines:
        particles.append(ParticleData(pid, line))
        pid += 1
    return particles

def runProgram1(inputfile):
    particles = loadParticles(inputfile)
    for i in range(0, 1000):
        for particle in particles:
            particle.tick()

    particles.sort(key=lambda x: x.distance, reverse=False)
    print("Part 1 Particle {} is closest with distance: {}".format(particles[0].id, particles[0].distance))

def runProgram2(inputfile):
    particles = loadParticles(inputfile)
    startsize = len(particles)

    for i in range(0, 1000):
        for particle in particles:
            particle.tick()
        particles = filter(notEliminated, particles)
        particles.sort(key=lambda x: (x.position.x, x.position.y, x.position.z), reverse=False)
        for x in range(1, len(particles)):
            if particles[x - 1].shareSamePosition(particles[x]):
                particles[x - 1].eliminated = True
                particles[x].eliminated = True
    print("Part 2 Particles at start:{}, at end: {}".format(startsize, len(particles)))

runProgram1("input.txt")
runProgram2("input.txt")
