package day02

import readInput

fun winConditionFulfilled(opp: String, mine: String): Boolean{
    return (opp == "A" && mine == "Y") ||
            (opp == "B" && mine == "Z") ||
            (opp == "C" && mine == "X")
}

fun loseConditionFulfilled(opp: String, mine: String): Boolean{
    return (opp == "A" && mine == "Z") ||
            (opp == "B" && mine == "X") ||
            (opp == "C" && mine == "Y")
}

fun rpsResult(opponent: String, mine: String): String {

    if (winConditionFulfilled(opponent, mine)) {
        return "w"
    }

    if (loseConditionFulfilled(opponent, mine)) {
        return "l"
    }

    return "d"
}

fun rpsReverse(opp: String, outc: String): String {
    val possibilities = listOf("X", "Y", "Z")

    // draw
    if (outc == "Y") return opp

    // win
    if (outc == "Z") {
        for (out in possibilities) {
            if (rpsResult(opp, out) == "w"){
                return out
            }
        }
    }

    // lose
    for (out in possibilities) {
        if (rpsResult(opp, out) == "l"){
            return out
        }
    }

    return "error"
}
fun main() {

    val values = mapOf(
        "A" to 1, // A, X = "Rock" # 1
        "X" to 1,
        "B" to 2, // B, Y = "Paper" # 2
        "Y" to 2,
        "C" to 3, // C, Z = "Scissors" # 3
        "Z" to 3
    )

    fun part1(input: List<String>): Int {

        var totalScore = 0
        for (jankenRound in input) {
            val (opp, mine) = jankenRound.split(" ")

            val chosenShapeVal = values[mine]

            val matchVal =
                when (rpsResult(opp, mine)) {
                    "w" -> 6
                    "d" -> 3
                    else -> 0
                }

            totalScore += chosenShapeVal?.plus(matchVal) ?: 0
        }

        return totalScore
    }

    fun part2(input: List<String>): Int {

        var totalScore = 0
        for (jankenRound in input) {
            val (opp, outc) = jankenRound.split(" ")

            val matchVal =
                when (outc) {
                    "Z" -> 6
                    "Y" -> 3
                    else -> 0
                }

            val neededShape = rpsReverse(opp, outc)

            val chosenShapeVal = values[neededShape]

            totalScore += chosenShapeVal?.plus(matchVal) ?: 0
        }

        return totalScore
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("day02/test_input")
    check(part1(testInput) == 15)

    val input = readInput("day02/input")
    println(part1(input))
    println(part2(input))
}
