package day03

import readInput

fun generateAsciiMap(): Map<Char, Int> {
    val asciiMap = mutableMapOf<Char, Int>()
    // a to z
    for (asciiVal in 97..122) {
        val char = asciiVal.toChar()
        asciiMap[char] = asciiVal-96
    }

    // A to Z
    for (asciiVal in 65..90) {
        val char = asciiVal.toChar()
        asciiMap[char] = asciiVal-38
    }
    return asciiMap
}

fun main() {

    val asciiMap = generateAsciiMap()
    /**
    a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, j=10, k=11, l=12, m=13, n=14, o=15, p=16, q=17, r=18, s=19, t=20, u=21, v=22, w=23, x=24, y=25, z=26,
    A=27, B=28, C=29, D=30, E=31, F=32, G=33, H=34, I=35, J=36, K=37, L=38, M=39, N=40, O=41, P=42, Q=43, R=44, S=45, T=46, U=47, V=48, W=49, X=50, Y=51, Z=52
    **/

    fun part1(input: List<String>): Int {

        val total = input.sumOf { rucksack ->
            val midPoint = rucksack.length/2
            val firstCompartment = rucksack.slice(0 until midPoint).toSet()
            val secondCompartment = rucksack.slice(midPoint until rucksack.length).toSet()

            val intersection = firstCompartment.intersect(secondCompartment).elementAt(0)
            asciiMap[intersection] ?: 0
        }

        return total
    }

    fun part2(input: List<String>): Int {

        val window = 3

        val total = input.chunked(window).sumOf {it ->
            val (firstGroup, secondGroup, thirdGroup) = it

            val intersection = firstGroup.toSet()
                .intersect(secondGroup.toSet())
                .intersect(thirdGroup.toSet())
                .elementAt(0)
            asciiMap[intersection]?: 0
        }

        return total
    }

    // test if implementation meets criteria from the description, like:
    val testInput = readInput("day03/test_input")
    check(part1(testInput) == 157)

    val input = readInput("day03/input")
    println(part1(input))
    println(part2(input))
}
