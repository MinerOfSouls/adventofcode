{:ok, contents} = File.read("day2_input.txt")
ranges = contents |> String.split(",", trim: true)

int_r = Enum.map(
  ranges,
  fn x ->
    Enum.map(
      String.split(x, "-"),
      fn x ->
        Integer.parse(x) |> elem(0)
      end
    )
  end
)

#and String.equivalent?(String.slice(x, 0, div(String.length(x), 2)), String.slice(x, div(String.length(x), 2)+1, div(String.length(x), 2)))

sum_part1 = Enum.reduce(
  int_r,
  0,
  fn ([x, y], acc) ->
    Enum.reduce(
      Enum.map(
        Enum.filter(
          Enum.map(x..y, fn x -> to_string(x) end),
          fn x ->
            rem(String.length(x), 2) == 0 and String.equivalent?(String.slice(x, 0, div(String.length(x), 2)), String.slice(x, div(String.length(x), 2), div(String.length(x), 2)))
          end
        ),
        fn x -> Integer.parse(x) |> elem(0) end
      ),
      0,
      fn (x, acc) -> x+acc end
    )+acc
  end
)
#28915664389
sum_part2 = Enum.reduce(
  int_r,
  0,
  fn ([x, y], acc) ->
    Enum.reduce(
      Enum.map(
        Enum.filter(
          Enum.map(x..y, fn x -> to_string(x) end),
          fn x ->
            elem(List.first(List.first((~r/#{Regex.escape(x)}/ |> Regex.scan(String.duplicate(x, 2), return: :index, offset: 1)))), 0) != String.length(x)
          end
        ),
        fn x -> Integer.parse(x) |> elem(0) end
      ),
      0,
      fn (x, acc) -> x+acc end
    )+acc
  end
)

IO.puts(sum_part2)
