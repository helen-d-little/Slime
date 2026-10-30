# Slime
Doing something interesting with slime mould as per Jeff Jones 1987 paper

So I've been thinking about this for a couple of years. Using [this paper](https://arxiv.org/pdf/1511.07654) as a starting point, I'd like to have a slime mould "happily" moving around in a matrix, then to do something along the lines of [this](https://www.thegreatplanet.org/tokyo-slime-mold-experiment/) then who knows? 

## Starting in the middle
As this is meant to be a "fun" exercise I'm staring in the middle of the paper with the particles properties.

- Population of mobile particles in a 2D diffuse environment
- Particles act independently
- Two phases
    - Sensory (sample the environment)
    - Motor (move in the environment)
- In the sensory phase the particle uses it's 3 forward-based sensors to rotate to the strongest local source of chemoattractant (food)
- In the motor phase the particle moves forward in it's current orientation as long as nothing is in it's way. If it's blocked it'll just rotate a random amount

The diffusion of the chemoattractant signals is a 3x3 filter kernel with the mean multiplied by a dampening factor set to 0.1.

I figure this is the first thing to do. Make the environment, add some chemoattractant and allow it to diffuse. 