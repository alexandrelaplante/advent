INPUT = """#############################################################################################################################################
#...#.......#.........#.#...........................#...........#...............#.#.................#.......#.........#.........#.......#..E#
#.#.#.#.###.#.#.#####.#.#.###.###.#.#################.#######.###.#############.#.#.#.#.#########.###.#####.#.#####.#.###.#######.###.#.#.#.#
#.........#.#.#.#...#.#.#...#.#.....#.........#.......#.....#.#...#.........#...#.#.#.#.........#.#...#.#...#.#.#...#...#.#.......#...#...#.#
#######.#.#.###.#.#.#.#.###.#.#######.#######.#.#########.#.#.#.#####.###.###.###.#.#.#########.#.#.###.#.#.#.#.#.#####.#.#.#######.#####.#.#
#...#...#.#.#...#.#...#...#.#.#.......#.....#.#.#.....#...#.#...#.....#...#...#.....#...#.......#.#.#...#.#.....................#...#.......#
#.#.#.###.#.#.###.#####.#.#.#.#.#######.###.#.#.#.#.#.#.#########.#########.#####.###.###.#########.#.#.#.#.#########.#.#.#####.#.###.#######
#.#.#.#...#...#.#...#...#.#.#...#.......#...#...#.#.#.#.........#.....#.....#...#...#.#...#.....#.....#.#.....#...............#.#...#...#...#
#.#.#.#.###.###.###.#.#.###.#######.###.#.#########.#.#######.#.#####.#.#####.#.###.#.#.#.#.###.#.#####.#.#.###.#######.#####.#.###.###.#.#.#
#.#.......................#.......#.#.....#.........#...............#.#.......#...#...#.#.#...#.#.#.....#...#...#...#...#.......#...#.#.#.#.#
#.#########.#.#.#####.###.#######.#.#.#########.#.#################.#.#######.###.###.#.#####.#.#.#.###.#.###.###.#.#.###.#######.###.#.#.#.#
#...#.........#...#.#...#.....#...#.#.#.......#.#.#...#.......#.....#...#...#...............#.#.#...#.#.#...#.#...#.#...#.#.#.....#...#...#.#
###.#.#.#####.###.#.###.###.#.#.###.#.###.###.###.###.#.###.###.#####.#.#.#.###.###.#.###.###.#.#####.#.#.#.#.#.###.###.#.#.#.#####.#######.#
#.........................#.#.#.....#.#...#.#...#...#.#...#...........#.#.#...#...#.#.#.#.....#.#.....#.....#.#.#.....#.#.#.#.....#.#.......#
#.###.#.#.#.#.#.#####.#####.#.#######.#.###.###.#.#.#.###.###########.###.###.###.#.#.#.#######.#.###.###.#.#.###.#####.#.#.#####.#.#.#######
#.#.#.#.#.#.#...#...#.#.....#.....#.#...#.....#.#.#.#...#...#...#.....#...#.#.....#.#.........#...#.#.......#...#...#...#.#.#.....#.#.....#.#
#.#.#.#.#.#.#.###.#.###.#########.#.#########.#.###.###.###.#.#.#######.###.#######.#########.#####.#####.###.#.#.#.#.###.#.#.#####.#####.#.#
#.#.....#...#.....#.#...#...#.....#...........#.....#.....#.#.#.........#...................#.#.........#.....#.#.#.#.#.....#.#.#.........#.#
#.#####.#.###.#####.#.#####.#.#######.#######.#######.#####.#.#####.#####.#####.#.###.###.###.#.#######.###.#.#.###.#.#######.#.#.#####.###.#
#.....#.#.#.......#.#...#...#...#.....#.......#.......#...#.#.#...#...#...#.....#...#...#.#...#.......#.#...#.#...#.....#.....#...#...#.....#
#.###.#.###.#.#####.###.#.#####.#.###.#.###.#.#.#.###.#.#.#.#.#.#.#.#.#.###.#.#####.###.###.###.#####.#.#.###.###.#####.#.#####.###.#.###.#.#
#.#...............#.....#.....#.#.#...#.#...#.#.#.#...#.#...#...#.#.#.#...#.........#.#.....#.#...#.#.#...#...#.#.....#...#.....#...#.#.#.#.#
#.#.###.#.#.#.###.#######.#.###.#.###.#.#.#####.#.#.###.#########.###.#.#.###########.#######.###.#.#.#####.###.#####.###.#####.#.###.#.#.#.#
#.#.#.#.#.............#...#.....#...#...#...#...#.#...#.#.......#...#...#...#...................#.#.#.#.....#.....#.#...#.#...#.#.#...#.....#
#.#.#.#.#####.#####.#.#.###########.###.#.#.#.###.###.#.#.#####.###.#.#.###.#.#.###############.#.#.#.#.#####.#.#.#.###.#.#.#.###.#.###.#####
#.#.#...#...#.......#.#...#.........#.....#.#.#...#...#.#.#.......#.#.#...#.#.#...............#.#.#.#.#.......#.#.#.....#.#.......#...#.#...#
###.#####.#.#.###########.#.#######.#.#####.#.#.###.###.#.#.#.#####.#.#.###.#.###############.###.#.#.###.#.###.#.###.#.###.###.#.###.###.#.#
#...#.....#.#.#.........#.#.....#...#.#...#...#.#.#...#.#.#.#.#.....#.#.....#...........#...#.#.....#.#.#...#...#...#.#.....#...#...#...#.#.#
#.###.#####.#.#.#######.#.#.###.#####.#.#.#####.#.###.#.###.#.#.#####.###########.#####.#.#.#.#.#####.#.###.#.#####.#.#######.#####.###.#.#.#
#...#...#...#...#.....#.......#.#.....#.#.....#.#.....#.....#.#.....#.........#...#...#...#.#.#.#.....#...#.#.....#.#.......#.....#...#...#.#
#.#.#.###.###.#.#.###.#####.###.#.#####.#####.#.#######.###.#.#####.#.###.###.#.###.#######.#.#.#.#####.###.#.###.#.#.#####.###.###.#######.#
#.#.......#...#...#...#...#.....#.#.#...#.#...#.........#...#.#.....#.....#...#...#.......#.#...#.#.......#.#...#.#...#.....#.#.............#
#######.###.#.#####.###.#.###.#.#.#.#.###.#.###.#########.#.###.###########.###.#.###.###.#.###.#.#######.#.#####.#####.#####.###.#.#.#####.#
#...#...#...#.#...#.....#.....#.#...#.#...#...#.........#.#.....#.........#.#...#...#.#...#...#.........#.#...#...#.........#.#...#.#.#...#.#
#.#.#.###.###.#.#.#####.#########.###.#.#.###.#######.###.#######.#######.#.#######.#.#.#####.#######.#.#.###.#.###########.#.#.###.#.#.#.#.#
#.#...#.....#.........#.#.........#...#.#...#.......#.#...#.....#.#.#...#...........#.#.....#.......#.#.#.......#.....#...#...#.....#...#...#
#.#####.#######.#####.#.#.#########.#####.#######.#.###.#.#.###.#.#.#.#.#.###.#######.#####.#######.###.#.#######.###.#.###.#########.#.#.###
#.#.....#.....#.#.....#.#.......#.#.....#.......#...#...#.#.#.#.....#.#...#.#.#...#.....#.#.......#...#.#.#.......#...#...#.#.....#.....#.#.#
#.#.#####.###.###.#########.###.#.#####.#.#.#####.###.###.#.#.#.#####.#.#.#.#.#.#.#####.#.#.#.#######.#.###.###.#.#.###.#.#.#.###.#.#.#.#.#.#
#.....#...#.#.....#...........#.....#.....#...#...#...#...#...#...#...#...#...#.#.....#...#.#.#.....#.#...#...#...#.#...#...#...#...#...#.#.#
#.#####.###.#####.#.###.#.###.#####.#.#######.#.###.#.#######.###.#.###.#######.###.#.#####.###.#.###.###.###.#####.###.#######.#####.#.#.#.#
#.#.....#.........#.#...#.......#...#.#.....#.......#.#...#...#.......#...........#...#.....#...#...#.....#...#...#...#.......#.#.....#.#...#
#.#.#########.#####.#.#.#########.###.#.###.###.#######.#.#.###.#####.#############.###.#####.#####.###.###.###.#.###.#####.###.#####.#.###.#
#.#.........#.......#.#.#...#...#.#.....#...#.....#.....#.........#.......#.#.....#...#.#.........#.#...#...#...#...#.#.........#.....#.....#
#.#########.###.#.###.#.#.#.#.#.#.#.#####.#.#.###.#.###.#########.#.#####.#.#.###.###.#.#.#######.#.#.###.###.#.#.#.#.#.###.#.###.###.#.#.###
#.#...#.....#...#...#.#.#.#.#.#...#...#...#.#...#.#.#.#...#...#...#...#.....#.#.#.....#.......#.......#...#...#.#.#...#...#.#.......#...#...#
#.#.#.#.#####.#####.#.#.#.#.#.#######.#.#####.###.#.#.#.#.#.#.#.###.#.#.#####.#.###.#########.#.#.#####.#######.#.#.###.#.###.#######.#.#.###
#...#...#...#.#...#.#...#.#...#.....#.#.....#.#...#.#.#.#...#.#.#...#.#.#.....#...#.#.....#.#.#.#.....#.#.....#.#.#...#.#.#...#.#...#.#.....#
###.#.###.#.#.#.#.#.#.###.#######.#.#.#####.#.#.###.#.#.#####.#.#####.#.#.#####.#.#.#.###.#.#.#.#######.#.###.#.#.###.###.#.###.#.#.#.###.#.#
#...#.#...#...#.#...#.....#.....#.#.......#...#...#.#.#.#.....#.......#.#...#...#.#.#.#.#.#.#.#.#.......#.#...#.#.#...#...#.....#.#.....#.#.#
#####.#.#######.#.#########.###.#.###.#########.#.#.#.#.#.###########.#.###.#.#.#.#.#.#.#.#.#.#.#.###.###.#.###.###.###.###.###.#.###.#.#.#.#
#.....#.#.......#.............#...#...#.......#.#.#.#.#.#.#.........#...#...#...#...#...#.#.#.#.#...#.#...#.#.#...#.....#.......#.#.......#.#
#.###.#.#.#######.###########.#######.#.#####.###.#.#.#.#.#.#.###.###.###.###.#########.#.#.#.#.###.###.###.#.#.#.#####.#.#######.###.###.#.#
#.#.....#.#...#.#.....#.....#.#.....#.#.#...#.#...#.#.#.#.#.....#.....#.#.......#.....#.#.#.......#.....#...#.#.#.......#...#...#.....#...#.#
#.#.#####.#.#.#.#####.###.###.#.###.###.###.#.#.#.#.#.#.#.#.###.#######.#.#####.#.###.#.#.#######.#######.###.#.###########.###.#####.#.#.#.#
#.#.....#...#.#...........#...#.#.......#...#.#.#.#.#...#.#.#.......#...#.....#.#.....#.#.....#.#.........#...#...#...#.....#...#.....#...#.#
#.#.#######.#.#####.#######.#.#.#########.###.#.###.#.#.#.#.#.#####.#.###.###.#.###.#.#.#####.#.#####.#.###.#.###.###.#.#####.###.#######.#.#
#.#.#.......#.....#...#.....#.#.....#.....#.....#.....#.#.#...#.......#...#...#.....#.....#...#.#...#.#.#...#...#.....#.......#...#...#...#.#
#.#.#.###.#######.#####.#####.#####.#.###.#.#####.#####.#.###########.#.###.###############.###.#.#.#.#.#.#.#######.###.#######.###.#.#.#.#.#
#.#.#...#...#.....#.....#...#.#...#.#.#...#.#.....#.....#.#...........#...#.................#...#.#.#.#.#.#...#...#.#...#.......#.#.#...#...#
#.###.#.#.#.#.#####.###.#.#.###.#.#.###.###.#.#####.#.###.#.#######.#.#.#.###################.###.#.#.#.#####.#.#.#.#.###.#######.#.#####.#.#
#.....#...#.#...#.....#.#.#...#.#.#...#.....#.....#.#...#.#.#...........#.#.........#.....#.......#...#.....#.#.#.#.#.#.#...#.#.............#
#.#####.#.#.###.###.#.###.#.#.#.#.###.#.#########.#.###.#.#.#.###########.#.#.#####.#####.#.#.#############.#.#.#.#.#.#.###.#.#.#########.#.#
#...............#...#.......#...#...#.#.#.#.........#...#...#.....#...#...#.#.#...#.......#.....#.....#.....#.#.#...#.#.#...#...#.#...#...#.#
###.#####.#.#.###.#.#.#####.#.###.#.#.#.#.#.#########.#############.#.###.#.#.#.#.#######.#####.###.#.#.#.###.#.#####.#.#.###.###.#.#.#.#.###
#...#.....#.#.....#.#.#.......#...#...#...#...#.......#.............#...#...#.#.#.#...#.........#...#.#.#.#.....#.#...#.#.#...#...#.#...#...#
#.###.#.#.#.#######.#.###.###.#.#####.###.###.#.###.###.###############.###.#.#.#.#.#.#####.#.#.#.###.#.#.#.#####.#.###.#.###.#.###.###.#.#.#
#...#.......#...#...#...#...#.......#.#.....#.#.#...#...#.........#...#...#.#.....#.#.....#.#...#.#.#.#...#.......#...#.#...#...#...#...#...#
#.#.#.#.#.###.#.#.#####.###.#######.#.#######.#.###.#.###.###.#.###.#.###.#.#####.#.#####.#.#####.#.#.#.#.#####.#####.#.###.#####.#.#.#.#.#.#
#.#.#.........#.#.#...#.#...#.......#.#...#...#...#.#.#.#.#...#.#...#...#.#.#...#.......#...#.....#...#.#.#.....#...#.....#.......#...#.#.#.#
#.#.###.#.#######.#.###.#.#.#.#####.#.#.#.#.#####.#.#.#.#.#.#####.#####.#.###.#.#######.#######.###.###.#.#######.#.#.#.#########.#.#.#.#.#.#
#.#.#.............#.......#.#.#...#.#.#.#...#.....#.#.#...#.....#...#.#.#.....#.......#.........#.#...#.#.......#.#...#...#.....#.....#...#.#
###.###.#.#.#######.#########.#.###.#.#.#####.#.#####.#.#######.###.#.#######.#######.#.#########.###.#.#######.#.#####.#.#.###.###.###.###.#
#...#.......#...#.....#...#...#.#...#...#...#.#.#.....#.......#.#...........#...#...#.......#...#...#...#...#.#.#.....#.#.#...#...#.....#.#.#
#.###.#.#####.#.#.#####.#.#.###.#.#######.#.#.#.#.###########.#.#.#####.###.###.#.#####.###.#.#.###.###.#.#.#.#.#.###.#.#.###.#.#.#.###.#.#.#
#.#...#.......#.#.#...#.#.#...#.#.#.......#...#.#.#.....#.....#.#.#.....#.#.#.....#.........#.#...#...#...#...#.......#.#.#...#.....#.......#
#.#.###.###.###.#.#.#.#.#.###.#.#.#.#.#.#.#.###.#.#.###.#######.#.#.#####.#.#######.#########.###.#.#########.#.#.#.#.#.#.#.###.###.###.#####
#.#.......#.#...#.#.#...#.....#...#.#.#...#.#...#.......#.....#.#...#.....#.........#...#.......#.#.........#.#...#.#.#.#.....#.#.....#...#.#
#.#######.#.#.###.#.###.#######.###.#.#####.#.#######.###.###.#.#####.#################.#.#####.#.#######.#.#.###.###.###.###.#.#.###.#.#.#.#
#...#.....#.#.....#.#...#...#.#.#...#...#...#.........#...#...#.....#...#.......#.....#...#.............#.#.....#...#.#...#.#.....#...#.#.#.#
#.###.#####.#######.#####.#.#.#.#######.#.#####.#########.#.###.###.#.#.#.###.#.#.#.#.#####.#.#########.###.#######.#.#.#.#.###.###.###.#.#.#
#.....#...#...#...#.#.....#.#.......#...#.#...#...........#.#.....#.#.#.......#...#.#.......#.........#...#.#.....#.....#.....#.....#...#...#
#.#####.#.###.#.#.#.#.#####.###.###.#.###.###.#.#.#########.#.#####.#.#############.#########.#####.#####.#.#.#.#.#######.#.###.###.#.#.###.#
#.#.....#.....#.#.#.......#.....#.....#.#.....#.#.........#.#.....#.....#.........#.#...#...#.#...#.#...#.#.#.#.#...#.......#...#.....#...#.#
#.###########.###.#######.#####.#######.#####.#.#########.#.#.#.#.#######.#####.#.#.#.#.#.#.#.###.#.#.#.#.#.#.#.###.#########.###.#.#####.#.#
#...........#.....#...#...#...#.......#.......#.........#.#.#.#.#.......#...#.......#.#...#.#.....#...#...#.#.#.#...#.......#.#.....#...#.#.#
###########.#######.#.#.###.#.#######.###########.#.#.###.#.###.#######.#.#.#####.#######.#.#####.###########.#.#.###.#####.#.###.#.#.#.###.#
#...#.....#...#.....#.#...#.#.....#.#.#...........#...#...#.#...#.....#.#.#.....#.......#.#.....#.#.....#...#.#.#...#.#...#.#...#.#...#...#.#
#.#.#.#.#.###.#.#####.###.###.###.#.#.#.#######.#.###.#.###.#.#######.#.#####.#.#.#.###.#.#.###.#.###.#.#.#.#.#.###.#.#.#.#.#.#.#.#.#####.#.#
#.#.#...#...#.#.#...#.........#.....#.#.#.....#.#.#...#.#...#.#.......#.....#.#.......#.#.#.#...#.#...#...#.#.#...#...#.#.#.#.#.#.#.....#.#.#
#.#.###.###.#.#.#.#.###.###.#######.#.#.#.#####.#.#.###.#.#.#.#.#####.#####.###.#######.#.#.#####.#.#######.#.#.#.#####.#.#.#.#.###.###.#.#.#
#.#.#...#.#...#...#...#...#.....#...#.#...#.....#.......#.#...#...........#...#.........#.#.#.....#...#.#.....#.#.......#.#.#.#.....#.#.#...#
#.#.#.#.#.#######.###.###.###.#.#.###.#.###.#####.#.#.###.#####.###.###.#.###.###.#######.#.#.#####.#.#.#.###########.###.#.#####.#.#.#.#.###
#.#.#.#...#.....#...#...#.....#.#.#.#...#...#.....#.#.#...#.........#.#.#...#.....#.#.....#.#.#.....#.#...#.......#...#...#.....#.....#.#...#
#.#.#.#.#.#.###.###.###.#######.#.#.#####.###.#####.#.#.#.#.#.#####.#.#.###.#######.#.#####.#.#######.#####.#####.#.###########.#.#.#.#.#.#.#
#.#.#.#.#...#...#.....#.#.......#.......#...#...#...#.#.#...#.#.....#.#...#.....#.......#...#.......#.......#.....#.....#.....#.#...#.#.#.#.#
###.#.#.#####.#######.#.#.#############.###.#.###.###.#######.#.#####.###.#######.#######.#########.#######.#.#####.###.#.#.#.#.#.#.#.#.#.#.#
#...#...#...#.#.....#.#.#.......#.......#...#.#...#...#.......#.#.......#.#.......#...#...#.......#.#.....#.#.#.....#.#...#.#.#.#.#.#.#.#.#.#
#.#####.#.#.#.#.###.#.#.#######.###.#####.#.###.###.###.###.#.#.#.#####.#.#.#####.#.#.#.###.#####.#.#.###.###.#####.#.#####.#.#.#.#.#.#.#.#.#
#.......#.#...#.....#.#.#.....#...#.#.....#.#...#.......#.....#.#.#.....#...#.......#.#.....#.#...#...#.#...#.....#.#.........#...#.#.#.#...#
#.###.#.#.#####.#.###.#.#.###.###.#.#.#.#####.###.###.#####.###.#.###############.###.#######.#.#######.###.#.###.#.###.###.#.###.#.#.#.###.#
#...#.#.#.......#.#...#.......#...#...#.#.....#.#.#.......#.#...#...............#.#.........#.#.......#...#.#...#.#...#.#...#.......#.#.....#
###.#.#.#########.#.#########.#.#.#.#####.#####.#.#######.#.#.###.###########.#.#.#########.#.#####.###.#.#.#.###.###.###.#.#####.###.###.#.#
#.#.#.#...#.....#.#.......#...#...#.#...#.....#.#.......#.#.#.#.........#.#...#.#.....#...#.......#.....#...#.#...#.#...#.#.#.......#...#.#.#
#.#.#.#.#.#####.#.#########.#####.#.#.#.#####.#.#.#####.#.#.#.#########.#.#.###.#.###.#.#.#######.#############.###.###.#.###.###.#.###.#.#.#
#.....#.#.#.....#.........#.#...#.#...#.#...#.#.#.......#.#.#...#.....#...#.#.#.......#.#.......#...#...........#...#...#.........#...#.#.#.#
#####.#.#.#.###.#########.#.#.#.#.#.###.#.#.#.#.#.#.#####.#.###.#.###.#####.#.#.#.#####.#######.###.#####.#.#####.###.#######.###.#.#.#.#.#.#
#...#.#.....#...#.......#...#.#...#...#...#...#.#.....#...#...#...#...#.....#.#.#.....#.......#...#.#.......#.....#...#.........#.#.#.#.#.#.#
#.#.#.#.#########.###.#######.###.#########.#.#.#####.#.###########.###.#####.#.#.###.#####.#####.#.#.#######.###.#.###.#######.#.#.###.#.###
#.#...#...........#.#.......#...#...........#.........#.#.........#.#...#.....#.#...#.....#.#.....#...#...#...#.#.#...#.#.....#.#.#.....#...#
#.#####.###########.#######.#.#.###########.#########.#.#.#####.###.#.#######.#.#########.#.#.###.#####.#.#.###.#.###.#.#####.#.#.#########.#
#.....#.#.#...........#.....#.#.........#...#.........#...#...#.#...#.#.......#.........#.#.#...#.#.....#...#...#...#...#.....#.#.#.....#.#.#
#.###.#.#.#.#.#####.###.###.#.#####.#####.###.#########.###.#.#.#.###.#.#.###.#########.#.#####.###.#########.#.###.#####.#.###.#.#.###.#.#.#
#.#...#.#...#.....#.#...#...#.....#.....#...#...#.....#...#.#.#...#.....#...#.......#...#.....#.....#.......#.#...#.......#.#...#.#.#.....#.#
###.#.#.#.###.###.#.#.#####.#####.#####.###.###.#.###.###.#.#######.#.#####.#.#######.#######.#.#####.#.###.#.#.#########.#.#.###.#.#######.#
#...#.#.#...#.#.....#.....#...#...#...#.....#...#.....#...#.......#.#.......#.#.....#.#.......#.#.........#...#.#.......#.#.#.#.#.#.#.....#.#
#.###.#.###.#.#.#.#.#####.#####.#####.#######.#####.#.#.#######.#.#.#####.#.###.###.#.#.#######.#.#########.#.#.#.#####.#.#.#.#.#.#.#.###.#.#
#.#...#.#.#.....#.#.....#.......#.......#.........#.#.........#.#...#.#.......#...#.#...#.....#.#.....#...#...#.....#...#.....#.....#.#.#.#.#
#.#####.#.###.###.###.#####.#####.#####.#####.###.#.#.#######.#.#####.#.#####.###.#.#######.###.###.###.#.###########.#########.#####.#.#.#.#
#.....#.#.........#.#.......#.....#.........#.#...#.........#.#.......#...#...#...#.......#...#.#.#.#...#.......#...#.#...#...#...#...#...#.#
#.###.#.#.###.#####.###.###.#####.#########.###.#####.#.#####.#######.###.#.#.#.###.#####.#.#.#.#.#.#.#########.#.#.#.#.#.#.#.###.#.###.###.#
#...#.#.#.#...........#.#.#.....#.....#.........#.....#.#...#.#.....#...#.#.#.#...#...#.#.#.#.#.#.#.#.#.....#...#.#.#...#...#...............#
###.#.#.#.#.#.#########.#.#####.#.###.###.#########.#####.#.#.#.#.#.###.#.#.###.#####.#.#.#.#.#.#.#.#.#####.#.###.#.#####.#####.#.#.#########
#...#...#.#.....#...............#...#.......#...#...#.....#.#.#.#.#.#...#.#.....#.....#...#.#.#.....#.....#...#...#.....#.#...#.#.#.........#
#.#######.#.#.#.#.###.###.###########.#####.#.#.#.#.#.#####.#.#.#.#.#.###.###.#.#.#######.###.#.###.#####.#.###.#######.#.#.###.#.#########.#
#.#.....#.#.#...#...#.....#...#.....#.#.......#.#.#.#.....#...#.#.#.#.#.#.......#.#.....#.....#...#...#...#.#.....#.....#.#.#...#.#.......#.#
#.#.###.#.###.#.###.#.###.#.#.#.###.#.#.#.#####.#.#######.#####.#.###.#.#####.#.#.#.###.#####.#.#.#####.###.#.###.#.#####.#.#.#.#.#.#######.#
#...#.#.#.#...#...#.....#.#.#.#.#.#.....#.#.....#.......#.....#.#...#.#.....#.#.#.#...#.#.......#.......#...#.#...#...#.....#.#.#.#.#.....#.#
#####.#.#.#.#.###.###.#.#.#.#.#.#.###.###.#.#######.###.#####.#.###.#.#.#####.#.#.###.#.#######.#########.#####.#####.#######.#.#.#.#.###.#.#
#.#.....#...#...#.....#.#...#...#.........#.....#...#.#...#...#...............#.#.....................#...#.....#.....#.....#.#.#.#...#...#.#
#.#.#########.#.#####.#.#.#####.#####.###.#.###.#.###.###.#.#.#######.#.#.#.#.#.#######.#######.#######.###.#####.#####.###.#.#.#.#####.###.#
#.#.#.........#...#.......................#...#.#...#...#.#...#.....#.#.#.....#.....#.........#.#...#...#...#.....#...#.#.....#.#.......#...#
#.#.#.#.#####.###.#.#.#.###.#.###.###.#.#.#####.#.#.###.#.###.#.###.#.#.###.#.#####.#.#####.#.#.#.#.#.###.###.#####.#.#.###############.#.###
#.#.#.#.#.....#...#...#.....#.........................#.#...#.#...#.#...#...#.....#...........#...#...#.....#.......#.#.#...#.....#.....#...#
#.#.#.#.#.#####.###############.#####.#.#########.###.#.#.###.###.#.#####.#.#.###.#.###.#.#.#.#.#######.###.#########.#.#.#.#.###.#.#######.#
#...#.#.#...#...#...............#...#.#...#.....#...#.#...#...#...#.......#.............#.#.#...........#...#...#...#.#...#.....#.#.......#.#
#.###.#.###.#.###.#.#.#.#####.###.#.#.###.#.###.###.#.###.#.#.#.###########.#.#####.#.###.#####.#######.#.###.###.#.#.#.#######.#.#####.###.#
#...#.#.#...#.#...#.................................#...#.#.#.....#...#...#.#.#.#...#...#.....#.......#.#...#.....#...#.......#.#.......#...#
###.###.#.###.#####.#.#.#.###.#.#####.###.#.#.###.#####.###.#.###.#.###.#.#.#.#.#.###.#.#####.#.#####.#####.#.#############.#.###########.#.#
#S......#...........#...#.......#...........#.........#...........#.....#.....#.......#.........#...........#...............#.............#.#
#############################################################################################################################################"""

TEST = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""


class Direction:
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3


def part1(INPUT) -> None:
    maze: list[list[str]] = [list(row) for row in INPUT.split("\n")]

    si, sj = 0, 0
    ei, ej = 0, 0
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                si, sj = i, j
            elif c == "E":
                ei, ej = i, j

    visited: dict[tuple[int, int, int], int] = {}  # (i, j, dir) -> score
    to_visit: list[tuple[int, int, int, int]] = []  # (i, j, dir, score)
    best = float("inf")
    to_visit.append((si, sj, Direction.EAST, 0))

    while to_visit:
        i, j, dir, score = to_visit.pop()
        if visited.get((i, j, dir), float("inf")) <= score:
            # we've already visited this spot with a better score
            continue

        if score >= best:
            # this can't beat the best path
            continue

        visited[(i, j, dir)] = score

        if (i, j) == (ei, ej):
            best = min(best, score)

        # each of 2 turns
        # TODO: optimization is only turn if no wall on that side,
        # since we never want to turn around or the wrong way
        to_visit.append((i, j, (dir + 1) % 4, score + 1000))
        to_visit.append((i, j, (dir - 1) % 4, score + 1000))

        # forwards
        io, jo = 0, 0  # offset
        if dir == Direction.EAST:
            io, jo = 0, 1
        if dir == Direction.NORTH:
            io, jo = -1, 0
        if dir == Direction.WEST:
            io, jo = 0, -1
        if dir == Direction.SOUTH:
            io, jo = 1, 0
        if maze[i + io][j + jo] != "#":
            to_visit.append((i + io, j + jo, dir, score + 1))

    print(best)


def part2(INPUT) -> None:
    maze: list[list[str]] = [list(row) for row in INPUT.split("\n")]

    si, sj = 0, 0
    ei, ej = 0, 0
    for i, row in enumerate(maze):
        for j, c in enumerate(row):
            if c == "S":
                si, sj = i, j
            elif c == "E":
                ei, ej = i, j

    visited: dict[
        tuple[int, int, int], tuple[int, list[tuple[int, int]]]
    ] = {}  # (i, j, dir) -> (score, path)
    to_visit: list[
        tuple[int, int, int, int, list[tuple[int, int]]]
    ] = []  # (i, j, dir, score, path)
    # best = float("inf")
    best = 98416  # from part 1
    to_visit.append((si, sj, Direction.EAST, 0, [(si, sj)]))
    best_tiles: set[tuple[int, int]] = set()

    # counter = 0
    while to_visit:
        # if counter % 10000 == 0:
        #     print(counter, len(visited), len(to_visit), best, len(best_tiles))
        # counter += 1
        path: list[tuple[int, int]]
        i, j, dir, score, path = to_visit.pop()
        visited_score = visited.get((i, j, dir), [float("inf")])[0]
        if visited_score < score:
            # we've already visited this spot with a better score
            continue

        if score > best:
            # this can't beat the best path
            continue

        visited[(i, j, dir)] = (score, path)

        if (i, j) == (ei, ej):
            if score < best:
                best = score
                best_tiles = set(path)
            elif score == best:
                best_tiles |= set(path)

        def get_offset(dir: int) -> tuple[int, int]:
            if dir == Direction.EAST:
                return 0, 1
            elif dir == Direction.NORTH:
                return -1, 0
            elif dir == Direction.WEST:
                return 0, -1
            elif dir == Direction.SOUTH:
                return 1, 0
            raise

        # right turn
        ri, rj = get_offset((dir + 1) % 4)
        if maze[i + ri][j + rj] != "#":
            to_visit.append((i, j, (dir + 1) % 4, score + 1000, path))

        # left turn
        li, lj = get_offset((dir - 1) % 4)
        if maze[i + li][j + lj] != "#":
            to_visit.append((i, j, (dir - 1) % 4, score + 1000, path))

        # forwards
        io, jo = get_offset(dir)
        if maze[i + io][j + jo] != "#":
            to_visit.append((i + io, j + jo, dir, score + 1, path + [(i, j)]))

    print(best)
    print(len(best_tiles) + 1)


part1(INPUT)
part2(INPUT)