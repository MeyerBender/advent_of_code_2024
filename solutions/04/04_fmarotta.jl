function read_matrix(file)
    l = readlines(file)
    [l[i][j] for i in eachindex(l), j in eachindex(l[1])]
end

function part1(m)
    count = 0
    for r in axes(m, 1), c in axes(m, 2)
        if 'X' != m[r, c]
            continue
        end
        for dr = (-1, 0, 1), dc = (-1, 0, 1)
            if 0 == dr == dc
                continue
            end
            nr, nc = r + dr, c + dc
            word = "MAS"
            while "" != word && checkbounds(Bool, m, nr, nc) && m[nr, nc] == word[1]
                word = word[2:end]
                nr, nc = nr + dr, nc + dc
            end
            if "" == word
                count += 1
            end
        end
    end
    return count
end

function part2(m)
    count = 0
    for r in 2:size(m, 1)-1, c in 2:size(m, 2)-1
        if 'A' != m[r, c]
            continue
        end
        q13 = (m[r-1, c+1], m[r+1, c-1])
        q24 = (m[r-1, c-1], m[r+1, c+1])
        x = (('M', 'S'), ('S', 'M'))
        if q13 in x && q24 in x
            count += 1
        end
    end
    count
end

m = read_matrix(ARGS[1])
part1(m) |> println
part2(m) |> println
