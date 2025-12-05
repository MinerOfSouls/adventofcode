file = read("2025/day4_input.txt", String)

rows = split(file, "\r\n")

mat = map(row -> map(x -> x == '@' ? 1 : 0, collect(row)), rows)

mat = permutedims(hcat(mat...))

mat2 = zeros((139, 139))

mat2[2:138, 2:138] .= mat

kernel = [1 1 1; 1 0 1; 1 1 1]

s = 0

for i in 2:138
    for j in 2:138
        s += sum(mat2[i-1:i+1, j-1:j+1].*kernel) < 4 && mat2[i, j] == 1 ? 1 : 0
    end
end

s2 = 0
removed = 0

while true
    for i in 2:138
        for j in 2:138
            if sum(mat2[i-1:i+1, j-1:j+1].*kernel) < 4 && mat2[i, j] == 1
                s2+=1
                removed +=1
                mat2[i,j] = 0.0
            end
        end
    end
    println(removed)
    if removed == 0
        break
    end
    removed = 0
end
