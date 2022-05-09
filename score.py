class Score:

    #defines the standalone class functions - accepts REST parameter
    def run(self, score):

        #file handling
        filename = "scores.txt"
        file = open(filename, "r")
        info = file.read()
        file.close()
        return info
