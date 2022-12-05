package day01
import readInput

fun main() {

    fun countTotalCalories(caloriesGroupList: List<String>): MutableSet<Int> {
        val totalCalories = mutableSetOf<Int>()
        var currentCal = 0
        for (calories in caloriesGroupList) {
            if (calories == "") {
                totalCalories.add(currentCal)
                currentCal = 0
            } else {
                currentCal += calories.toInt()
            }
        }

        return totalCalories
    }

    fun part1(input: List<String>): Int {
        val caloriesGroupList = input.toMutableList()
        caloriesGroupList.add("")

        return countTotalCalories(caloriesGroupList).max()
    }

    fun part2(input: List<String>): Int {
        val caloriesGroupList = input.toMutableList()
        caloriesGroupList.add("")

        val totalCalories = countTotalCalories(caloriesGroupList)

        var combinedCalories = 0
        for ( i in 1..3) {
            val currentHighest = totalCalories.max()
            combinedCalories += currentHighest
            totalCalories.remove(currentHighest)
        }

        return combinedCalories
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("day01/test_input")
    check(part1(testInput) == 24000)
    check(part2(testInput) == 45000)

    val input = readInput("day01/input")
    println(part1(input))
    println(part2(input))
}
