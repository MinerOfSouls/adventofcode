{:ok, contents} = File.read("day3_input.txt")
banks = contents |> String.split("\r\n", trim: true)

batteries = Enum.map(
  banks,
  fn x -> Integer.digits(Integer.parse(x) |> elem(0)) end
)

good = Enum.map(
  batteries,
  fn bank ->
    Enum.map(
      Enum.scan(
      bank,
      {0, 0},
      fn x, {max1, max2} ->
        cond do
          max1 == 0 ->
            {x, 0}
          max2 == 0 ->
            {max1, x}
          max2 > max1 ->
            {max2, x}
          x >= max2 ->
            {max1, x}
          true ->
            {max1, max2}
        end
      end
      ),
      fn {x, y} -> if x == 0 or y == 0 do 0 else 10*x+y end end
    )
  end
)

answer1 = Enum.reduce(
  good,
  0,
  fn list,acc -> Enum.max(list)+acc end
)

IO.puts(answer1)

good2 = Enum.map(
  batteries,
  fn bank ->
    Enum.map(
      Enum.scan(
      bank,
      Enum.map(1..12, fn _x -> 0 end),
      fn x, maxes ->
        cond do
          Enum.find_index(maxes, fn x -> x == 0 end) != nil ->
            List.replace_at(maxes, Enum.find_index(maxes, fn x -> x == 0 end), x)
          Enum.any?(Enum.map_reduce(Enum.reverse(maxes),x,fn n, perv -> {n-perv, n} end) |> elem(0), fn i -> i < 0 end) ->
            elem(List.pop_at(maxes,Enum.find_index(Enum.reverse(Enum.map_reduce(Enum.reverse(maxes),x,fn n, perv -> {n-perv, n} end) |> elem(0)), fn i -> i < 0 end)), 1) ++ [x]
          true ->
            maxes
        end
      end
      ),
      fn x -> Enum.reduce(x, fn x, acc -> 10*acc + x end) end
    )
  end
)

answer2 = Enum.reduce(
  good2,
  0,
  fn list,acc -> Enum.max(list)+acc end
)

IO.puts(answer2)
