{:ok, contents} = File.read("day8_input.txt")

to_int = fn x -> Integer.parse(x) |> elem(0) end

boxes = contents |> String.split("\r\n", trim: true) |> Enum.map(fn x -> String.split(x, ",", trim: true) |> Enum.map(to_int) |> List.to_tuple() end)

distance = fn {x1, y1, z1}, {x2, y2, z2} -> (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 end

distances = Enum.map(
  boxes,
  fn box ->
    {box, Enum.sort_by(Enum.map(boxes, fn b2 -> {distance.(box, b2), b2} end), &elem(&1, 0)) |> Enum.filter(fn {d, _b} -> d != 0 end)}
  end
)

defmodule Cmap do
  def tuple_unpacker({a, b}, c) do {c, b, a} end
  def tuple_repacker({a, b, c}, maps) do {MapSet.put(maps, {a, b}) |> MapSet.put({b, a}), c} end
  def path_exists(a, b, edges, visited) do
    if MapSet.member?(edges, {a, b})
    do
      true
    else
      if MapSet.filter(edges, fn {x, y} -> x == a and not MapSet.member?(visited, {x, y})  end) |> MapSet.size() == 0
      do
        false
      else
        Enum.any?(MapSet.filter(edges, fn {x, _y} -> x == a end) |> MapSet.to_list(), fn {_x, y} -> path_exists(y, b, edges, MapSet.put(visited, {a, b})) end)
      end
    end
  end

  def connection_map({connections, prev_l}, distances, count) when count > 0 do
    nc = Enum.reduce(
        distances,
        {{}, {}, -1},
        fn {box1, d_list}, {b1, b2, prev_bd} ->
          cond do
            prev_bd == -1 and Enum.find(d_list, fn {d, box2} -> d >= prev_l and not MapSet.member?(connections, {box1, box2})  end) != nil->
              tuple_unpacker(Enum.find(d_list, fn {d, box2} -> d >= prev_l and not MapSet.member?(connections, {box1, box2}) end), box1)
            prev_bd == -1 ->
              {{}, {}, -1}
            Enum.find(d_list, fn {d, box2} -> d >= prev_l and d < prev_bd and not MapSet.member?(connections, {box1, box2}) end) != nil ->
              tuple_unpacker(Enum.find(d_list, fn {d, box2} -> d >= prev_l and d < prev_bd and not MapSet.member?(connections, {box1, box2}) end), box1)
            true ->
              {b1, b2, prev_bd}
            end end
      )
    connection_map(
      tuple_repacker(
      nc, connections),
    Enum.map(distances, fn {b, d} -> if b == elem(nc, 0) or b == elem(nc, 1) do {b, List.delete(d, 0)} else {b, d} end end),
    count-1
    )
  end
  def connection_map({connections, _prev_l}, _distances, 0) do connections end

  def find_top_components(connections, top) do
    connections = MapSet.to_list(connections)
    check_parts = fn b, map -> Enum.find(Map.keys(map), fn k -> Enum.find_value(map[k], &(&1 == b)) end) end
    componets = Enum.reduce(
      connections,
      {%{}, 1},
      fn {b1, b2},{map, i} ->
        cond do
          check_parts.(b1, map) == nil and check_parts.(b2, map) == nil ->
            {Map.update(map, i, [b1, b2], fn x -> [b2 | [b1 | x]] end), i+1}
          check_parts.(b2, map) == nil ->
            {Map.update(map, check_parts.(b1, map), -1, fn x -> [b2 | x] end), i}
          check_parts.(b1, map) == nil ->
            {Map.update(map, check_parts.(b2, map), -1, fn x -> [b1 | x] end), i}
          check_parts.(b1, map) == check_parts.(b2, map) ->
            {map, i}
          check_parts.(b1, map) != check_parts.(b2, map) ->
            {Map.update(map, check_parts.(b1, map), -1, fn x -> x ++ map[check_parts.(b2, map)] end) |> Map.delete(check_parts.(b2, map)),i}
        end
      end)
  elem(componets, 0)|> Map.to_list() |> Enum.map(fn t -> elem(t, 1) end) |> Enum.map(fn x -> Enum.count(x) end) |> Enum.sort() |> Enum.reverse() |> Enum.take(top)
  end

  def how_many_components({b1, b2, _d}, i, map, distances) do
    check_parts = fn b, map -> Enum.find(Map.keys(map), fn k -> Enum.find_value(map[k], &(&1 == b)) end) end
    {map, i} = cond do
          b1 == -1 and b2 == -1 ->
            {map, i}
          check_parts.(b1, map) == nil and check_parts.(b2, map) == nil ->
            {Map.update(map, i, [b1, b2], fn x -> [b2 | [b1 | x]] end), i+1}
          check_parts.(b2, map) == nil ->
            {Map.update(map, check_parts.(b1, map), -1, fn x -> [b2 | x] end), i}
          check_parts.(b1, map) == nil ->
            {Map.update(map, check_parts.(b2, map), -1, fn x -> [b1 | x] end), i}
          check_parts.(b1, map) == check_parts.(b2, map) ->
            {map, i}
          check_parts.(b1, map) != check_parts.(b2, map) ->
            {Map.update(map, check_parts.(b1, map), -1, fn x -> x ++ map[check_parts.(b2, map)] end) |> Map.delete(check_parts.(b2, map)),i}
        end
    in_net = map |> Map.to_list() |> Enum.map(fn t -> elem(t, 1) end) |> Enum.concat()
    singles = Enum.map(distances, fn {b, _d} -> b end) |> Enum.filter(fn {x1, y1, z1} -> not Enum.any?(in_net, fn {x2, y2, z2} -> x1 == x2 and y1 == y2 and z1 == z2 end) end)
    {(map |> Map.to_list() |> Enum.count()) + Enum.count(singles), map, i}
  end

  def connect_until_one({connections, prev_l}, distances, last_cc, map, i) do
    {c, map, i} = how_many_components(last_cc, i, map, distances)
    IO.inspect(c)
    if c == 1 do last_cc else
    nc = Enum.reduce(
        distances,
        {{}, {}, -1},
        fn {box1, d_list}, {b1, b2, prev_bd} ->
          cond do
            prev_bd == -1 and Enum.find(d_list, fn {d, box2} -> d >= prev_l and not MapSet.member?(connections, {box1, box2}) end) != nil ->
              tuple_unpacker(Enum.find(d_list, fn {d, box2} -> d >= prev_l and not MapSet.member?(connections, {box1, box2}) end), box1)
            prev_bd == -1 ->
              {{}, {}, -1}
            Enum.find(d_list, fn {d, box2} -> d >= prev_l and d < prev_bd and not MapSet.member?(connections, {box1, box2}) end) != nil->
              tuple_unpacker(Enum.find(d_list, fn {d, box2} -> d >= prev_l and d < prev_bd and not MapSet.member?(connections, {box1, box2}) end), box1)
            true ->
              {b1, b2, prev_bd}
            end end
      )
    connect_until_one(tuple_repacker(nc, connections),Enum.map(distances, fn {b, d} -> if b == elem(nc, 0) or b == elem(nc, 1) do {b, List.delete(d, 0)} else {b, d} end end),nc, map, i)
    end
  end
end

#IO.inspect(Cmap.connection_map({MapSet.new(), 0}, distances, 1000) |> Cmap.find_top_components(3))

IO.inspect(Cmap.connect_until_one({MapSet.new(), 0}, distances,{-1, -1, -1}, %{}, 1))
