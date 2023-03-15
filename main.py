from snake.game import Game, GameConf, GameMode

greedy = "GreedySolver"
hamilton = "HamiltonSolver"

normal = GameMode.NORMAL

conf = GameConf()
conf.solver_name = greedy
conf.model = normal
print("solver: %S " % (conf.solver_name))
print("Mode: %S" %(conf.mode))
Game(conf).run()