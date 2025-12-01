
{:ok, contents} = File.read("day1_input.txt")
instrutions = contents |> String.split("\r\n", trim: true)

int_i = Enum.map_every(instrutions, 1,
fn x ->
  if String.at(x, 0) == "L"
  do
    -(Integer.parse(String.slice(x, 1, String.length(x)-1)) |> elem(0))
  else
    Integer.parse(String.slice(x, 1, String.length(x)-1)) |> elem(0)
  end end)

changes = Enum.scan(int_i, 50, fn (x, acc) -> Integer.mod(acc+x, 100) end)

password = Enum.count(changes, fn x -> x == 0 end)

IO.puts(password)

full = Enum.scan(
  int_i,
  {50, 0},
  fn (x, {acc, _y}) ->
    {
      Integer.mod(acc+x, 100),
      Enum.count(
        Enum.map(
          (acc + (if acc+x < acc do -1 else 1 end))..(acc+x)//(if acc+x < acc do -1 else 1 end),
          fn y -> Integer.mod(y, 100) end
          ),
          fn z -> z == 0 end
        )
    }
  end)

pas2 = Enum.reduce(full, 0, fn ({_x, y}, acc) -> y+acc end)
