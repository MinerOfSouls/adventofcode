{:ok, contentsa} = File.read("day5a_input.txt")
ranges = contentsa |> String.split("\r\n", trim: true) |> Enum.map(fn x-> Enum.map(String.split(x,"-"), fn n -> Integer.parse(n) |> elem(0) end) end)

{:ok, contentsb} = File.read("day5b_input.txt")
numbers = contentsb |> String.split("\r\n", trim: true) |> Enum.map(fn x-> Integer.parse(x) |> elem(0) end)

freshno = Enum.reduce(
  numbers,
  0,
  fn n, acc ->
    (if Enum.any?(ranges, fn [s, e] -> s <= n and n <= e end) do 1 else 0 end) + acc
  end
)

IO.puts(freshno)

fresh_ranges = ranges
  |> Enum.sort(fn [s1, e1], [s2, e2] -> if s1 == s2 do e1 >= e2 else s1 < s2 end end)
  |> Enum.map_reduce([0, 0], fn [s, e], [ps, pe] -> {if pe >= s do if pe>= e do [-1, pe] else [pe + 1, e] end else [s, e] end,if pe >= s do if pe>= e do [pe+1, pe] else [pe + 1, e] end else [s, e] end} end) |> elem(0)

fresh_numbers = Enum.reduce(fresh_ranges, 0, fn [s, e], acc -> if s != -1 do e-s+1+acc else acc end end)
IO.puts(fresh_numbers)
