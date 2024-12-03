function compute(file)
    part1 = 0
    part2 = 0
    go = true
    for l in eachline(file)
        for m in eachmatch(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", l)
            if m.match == "do()"
                go = true
            elseif m.match == "don't()"
                go = false
            elseif startswith(m.match, "mul")
                println(m.match)
                result = 1
                for s in eachsplit(m.match[5:end-1], ",")
                    result *= parse(Int, s)
                end
                part1 += result
                if go == true
                    part2 += result
                end
            end
        end
    end
    println(part1)
    println(part2)
end

compute(ARGS[1])
