from crispy.controller import CrispyController
from crispy.crypto.mime import Mime

if __name__ == "__main__":
    cc = CrispyController("localhost", 8080, Mime())
    cc.run()
    