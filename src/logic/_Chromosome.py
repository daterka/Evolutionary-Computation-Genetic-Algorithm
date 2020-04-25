from src.logic.configuration._Configuration import Config

class Chromosome(Config):
    # TODO constructor overloading
    def __init__(self, representation=[], length=None):
        self.representation = representation
        self.length = length
        # TODO count target at initiation?
        # self.target_value = None
        # self.x1_decimal = None
        # self.x2_decimal = None

    def __repr__(self):
        return repr(self.representation)

    @classmethod
    def constructFromParent(cls, parent):
        return cls(parent.get(), parent.len())

    def get(self):
        return self.representation

    def len(self):
        return len(self.representation)

    def decode_x1(self, reversed_rep):
        x1 = 0
        for i in range(0, self.x1_length):
            power = pow(2, i)
            x1 += reversed_rep[i] * power;

        domain_len = abs(self.x1_b - self.x1_a)
        fraction = domain_len / (pow(2, self.x1_length) - 1)
        x1 = self.x1_a + x1 * fraction
        return x1

    def decode_x2(self, reversed_rep):
        x2 = 0
        power_i = 0
        for i in range(self.x1_length, self.chromosome_length):
            power = pow(2, power_i)
            x2 += reversed_rep[i] * power
            power_i += 1

        domain_len = abs(self.x2_b - self.x2_a)
        fraction = domain_len / (pow(2, self.x2_length) - 1)
        x2 = self.x2_a + x2 * fraction
        return x2

    # TODO modify to decode chrom representing more than two args
    # TODO recode mote efficient
    def decode(self):
        reversed_repr = list(reversed(self.representation))
        x1 = self.decode_x1(reversed_repr)
        x2 = self.decode_x2(reversed_repr)
        args = (x1, x2)
        return args

    # def setTargetValue(self, target_val):
    #     self.target_value = target_val

    def getTargetValue(self):
        return self.target(self.decode())

    # def evaluate(self):
    #     return self.target(self.decode())
    #
    # def validate(self):
    #     pass

