{:ok, contents} = File.read("day6_input.txt")
equations1 = contents |> String.split("\r\n", trim: true) |> Enum.map(&(String.split(&1))) |> Enum.zip()

to_int = fn x -> Integer.parse(x) |> elem(0) end

grand_total = Enum.reduce(
  equations1,
  0,
  fn {one, two, three, four, symbol}, acc ->
    if symbol == "+"
    do to_int.(one) + to_int.(two) + to_int.(three) + to_int.(four) + acc
    else
      (to_int.(one) * to_int.(two) * to_int.(three) * to_int.(four)) + acc
    end end)

equations2 = contents |> String.split("\r\n", trim: true) |> Enum.map(&(String.split(&1, "", trim: true))) |> Enum.zip()

to_number = fn one, two, three, four ->
  Integer.undigits(Enum.map(Enum.filter([one, two, three, four], fn x -> x != " " end), to_int))
end

grand_total_actual = Enum.reduce(
  equations2,
  {0, 0, " "},
  fn {one, two, three, four, op}, {acc, subtotal, saved_op} ->
    cond do
      one == " " and two == " " and three == " " and four == " " and op == " " ->
        {acc + subtotal, 0, " "}
      saved_op == " " and op != " " ->
        {acc, to_number.(one, two, three, four), op}
      saved_op != " " ->
        if saved_op == "+" do {acc, subtotal + to_number.(one, two, three, four), saved_op} else {acc, subtotal * to_number.(one, two, three, four), saved_op} end
    end
  end
)

IO.puts(elem(grand_total_actual, 0) + elem(grand_total_actual, 1))
