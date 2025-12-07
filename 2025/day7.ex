{:ok, contents} = File.read("day7_input.txt")
layers = contents |> String.split("\r\n", trim: true) |> Enum.map(fn x -> String.split(x, "", trim: true) |> Enum.with_index() end)
important = Enum.map(layers, fn l -> Enum.filter(l, fn {x, _i} -> x == "^" or x == "S" end) end) |> Enum.filter(fn x -> x != [] end)

splits = Enum.reduce(
  important,
  {0, MapSet.new()},
  fn splitters, {s_sum, beams} ->
    Enum.reduce(
      splitters,
      {s_sum, beams},
      fn {s, i}, {s_subsum, beams_sub} ->
        cond do
          s == "S" ->
            {0, MapSet.put(beams_sub, i)}
          s == "^" ->
            if MapSet.member?(beams, i) do {s_subsum+1, MapSet.delete(beams_sub, i) |> MapSet.put(i-1) |> MapSet.put(i+1)} else {s_subsum, beams_sub} end
        end
      end
    )
  end
)

timelines = Enum.reduce(
  important,
  %{},
  fn splitters, beam_map ->
    Enum.reduce(
      splitters,
      beam_map,
      fn {s, i}, sub_beam_map ->
        cond do
          s == "S" ->
            Map.put(beam_map, i, 1)
          s == "^" ->
            if Map.has_key?(beam_map, i) do
              Map.delete(sub_beam_map, i) |> Map.update(i-1, beam_map[i], fn x -> x + beam_map[i] end) |> Map.update(i+1, beam_map[i], fn x -> x + beam_map[i] end)
            else
              sub_beam_map
            end
        end
      end
    )
  end
) |> Map.to_list() |> Enum.reduce(0, fn {_i, t}, acc -> t+acc end)
