'''
Every hex is a node in a graph. A hex has 0-6 "exits", which are graph 
connections to another hex. The graph can only be traversed randomly, which 
makes the graph an engine for procedural generation of arbitrary things.
'''

from random import randrange


class Hex(object):
    def __init__(self, id):
        self.id = id
        self.type = None
        self.connections = []

    def __str__(self):
        return str({
            "id": self.id,
            "connections": self.connections
        })

    def get_connection_by_direction(self, direction):
        return list(filter(lambda x: x["direction"] == direction, self.connections))[0]

    def delete_connection_by_direction(self, direction):
        # actually just sets the connection to self
        this_c = self.get_connection_by_direction(direction)
        this_c["hex"] = self

    def get_next(self, roll):
        if roll == 12:
            return self.get_connection_by_direction("a")
        if roll == 2 or roll == 3:
            return self.get_connection_by_direction("b")
        if roll == 4 or roll == 5:
            return self.get_connection_by_direction("c")
        if roll == 6 or roll == 7:
            return self.get_connection_by_direction("d")
        if roll == 8 or roll == 9:
            return self.get_connection_by_direction("e")
        if roll == 10 or roll == 11:
            return self.get_connection_by_direction("f")

    


'''
A typical hex flower contains 19 hexes. More or less may be possible, but we 
can stick with the basic flower for now.
'''
class HexFlower(object):
    def __init__(self, name):
        self.name = name
        self.hexes = []

        # Initialize the hexes
        for i in range(19):
            this_hex = Hex(i+1)
            self.hexes.append(this_hex)

        # now build connections
        # If we were using real coordinates, this would be programmatically easier
        flower = self
        hex_1 = flower.get_hex_by_id(1)
        hex_1.connections.append({"direction": "a", "hex": flower.get_hex_by_id(5)})
        hex_1.connections.append({"direction": "b", "hex": flower.get_hex_by_id(3)})
        hex_1.connections.append({"direction": "c", "hex": flower.get_hex_by_id(3)})
        hex_1.connections.append({"direction": "d", "hex": flower.get_hex_by_id(1)})
        hex_1.connections.append({"direction": "e", "hex": flower.get_hex_by_id(2)})
        hex_1.connections.append({"direction": "f", "hex": flower.get_hex_by_id(2)})

        hex_2 = flower.get_hex_by_id(2)
        hex_2.connections.append({"direction": "a", "hex": flower.get_hex_by_id(7)})
        hex_2.connections.append({"direction": "b", "hex": flower.get_hex_by_id(5)})
        hex_2.connections.append({"direction": "c", "hex": flower.get_hex_by_id(1)})
        hex_2.connections.append({"direction": "d", "hex": flower.get_hex_by_id(16)})
        hex_2.connections.append({"direction": "e", "hex": flower.get_hex_by_id(11)})
        hex_2.connections.append({"direction": "f", "hex": flower.get_hex_by_id(4)})

        hex_3 = flower.get_hex_by_id(3)
        hex_3.connections.append({"direction": "a", "hex": flower.get_hex_by_id(8)})
        hex_3.connections.append({"direction": "b", "hex": flower.get_hex_by_id(6)})
        hex_3.connections.append({"direction": "c", "hex": flower.get_hex_by_id(9)})
        hex_3.connections.append({"direction": "d", "hex": flower.get_hex_by_id(18)})
        hex_3.connections.append({"direction": "e", "hex": flower.get_hex_by_id(1)})
        hex_3.connections.append({"direction": "f", "hex": flower.get_hex_by_id(5)})

        hex_4 = flower.get_hex_by_id(4)
        hex_4.connections.append({"direction": "a", "hex": flower.get_hex_by_id(9)})
        hex_4.connections.append({"direction": "b", "hex": flower.get_hex_by_id(7)})
        hex_4.connections.append({"direction": "c", "hex": flower.get_hex_by_id(2)})
        hex_4.connections.append({"direction": "d", "hex": flower.get_hex_by_id(14)})
        hex_4.connections.append({"direction": "e", "hex": flower.get_hex_by_id(16)})
        hex_4.connections.append({"direction": "f", "hex": flower.get_hex_by_id(1)})

        hex_5 = flower.get_hex_by_id(5)
        hex_5.connections.append({"direction": "a", "hex": flower.get_hex_by_id(10)})
        hex_5.connections.append({"direction": "b", "hex": flower.get_hex_by_id(8)})
        hex_5.connections.append({"direction": "c", "hex": flower.get_hex_by_id(3)})
        hex_5.connections.append({"direction": "d", "hex": flower.get_hex_by_id(1)})
        hex_5.connections.append({"direction": "e", "hex": flower.get_hex_by_id(2)})
        hex_5.connections.append({"direction": "f", "hex": flower.get_hex_by_id(7)})


        hex_6 = flower.get_hex_by_id(6)
        hex_6.connections.append({"direction": "a", "hex": flower.get_hex_by_id(11)})
        hex_6.connections.append({"direction": "b", "hex": flower.get_hex_by_id(2)})
        hex_6.connections.append({"direction": "c", "hex": flower.get_hex_by_id(17)})
        hex_6.connections.append({"direction": "d", "hex": flower.get_hex_by_id(16)})
        hex_6.connections.append({"direction": "e", "hex": flower.get_hex_by_id(3)})
        hex_6.connections.append({"direction": "f", "hex": flower.get_hex_by_id(8)})

        hex_7 = flower.get_hex_by_id(7)
        hex_7.connections.append({"direction": "a", "hex": flower.get_hex_by_id(12)})
        hex_7.connections.append({"direction": "b", "hex": flower.get_hex_by_id(10)})
        hex_7.connections.append({"direction": "c", "hex": flower.get_hex_by_id(5)})
        hex_7.connections.append({"direction": "d", "hex": flower.get_hex_by_id(2)})
        hex_7.connections.append({"direction": "e", "hex": flower.get_hex_by_id(4)})
        hex_7.connections.append({"direction": "f", "hex": flower.get_hex_by_id(9)})

        hex_8 = flower.get_hex_by_id(8)
        hex_8.connections.append({"direction": "a", "hex": flower.get_hex_by_id(13)})
        hex_8.connections.append({"direction": "b", "hex": flower.get_hex_by_id(11)})
        hex_8.connections.append({"direction": "c", "hex": flower.get_hex_by_id(6)})
        hex_8.connections.append({"direction": "d", "hex": flower.get_hex_by_id(3)})
        hex_8.connections.append({"direction": "e", "hex": flower.get_hex_by_id(5)})
        hex_8.connections.append({"direction": "f", "hex": flower.get_hex_by_id(10)})

        hex_9 = flower.get_hex_by_id(9)
        hex_9.connections.append({"direction": "a", "hex": flower.get_hex_by_id(14)})
        hex_9.connections.append({"direction": "b", "hex": flower.get_hex_by_id(12)})
        hex_9.connections.append({"direction": "c", "hex": flower.get_hex_by_id(7)})
        hex_9.connections.append({"direction": "d", "hex": flower.get_hex_by_id(4)})
        hex_9.connections.append({"direction": "e", "hex": flower.get_hex_by_id(18)})
        hex_9.connections.append({"direction": "f", "hex": flower.get_hex_by_id(3)})

        hex_10 = flower.get_hex_by_id(10)
        hex_10.connections.append({"direction": "a", "hex": flower.get_hex_by_id(15)})
        hex_10.connections.append({"direction": "b", "hex": flower.get_hex_by_id(13)})
        hex_10.connections.append({"direction": "c", "hex": flower.get_hex_by_id(8)})
        hex_10.connections.append({"direction": "d", "hex": flower.get_hex_by_id(5)})
        hex_10.connections.append({"direction": "e", "hex": flower.get_hex_by_id(7)})
        hex_10.connections.append({"direction": "f", "hex": flower.get_hex_by_id(12)})

        hex_11 = flower.get_hex_by_id(11)
        hex_11.connections.append({"direction": "a", "hex": flower.get_hex_by_id(16)})
        hex_11.connections.append({"direction": "b", "hex": flower.get_hex_by_id(4)})
        hex_11.connections.append({"direction": "c", "hex": flower.get_hex_by_id(17)})
        hex_11.connections.append({"direction": "d", "hex": flower.get_hex_by_id(6)})
        hex_11.connections.append({"direction": "e", "hex": flower.get_hex_by_id(8)})
        hex_11.connections.append({"direction": "f", "hex": flower.get_hex_by_id(13)})

        hex_12 = flower.get_hex_by_id(12)
        hex_12.connections.append({"direction": "a", "hex": flower.get_hex_by_id(17)})
        hex_12.connections.append({"direction": "b", "hex": flower.get_hex_by_id(15)})
        hex_12.connections.append({"direction": "c", "hex": flower.get_hex_by_id(10)})
        hex_12.connections.append({"direction": "d", "hex": flower.get_hex_by_id(7)})
        hex_12.connections.append({"direction": "e", "hex": flower.get_hex_by_id(9)})
        hex_12.connections.append({"direction": "f", "hex": flower.get_hex_by_id(14)})

        hex_13 = flower.get_hex_by_id(13)
        hex_13.connections.append({"direction": "a", "hex": flower.get_hex_by_id(18)})
        hex_13.connections.append({"direction": "b", "hex": flower.get_hex_by_id(16)})
        hex_13.connections.append({"direction": "c", "hex": flower.get_hex_by_id(11)})
        hex_13.connections.append({"direction": "d", "hex": flower.get_hex_by_id(8)})
        hex_13.connections.append({"direction": "e", "hex": flower.get_hex_by_id(10)})
        hex_13.connections.append({"direction": "f", "hex": flower.get_hex_by_id(15)})

        hex_14 = flower.get_hex_by_id(14)
        hex_14.connections.append({"direction": "a", "hex": flower.get_hex_by_id(4)})
        hex_14.connections.append({"direction": "b", "hex": flower.get_hex_by_id(17)})
        hex_14.connections.append({"direction": "c", "hex": flower.get_hex_by_id(12)})
        hex_14.connections.append({"direction": "d", "hex": flower.get_hex_by_id(9)})
        hex_14.connections.append({"direction": "e", "hex": flower.get_hex_by_id(19)})
        hex_14.connections.append({"direction": "f", "hex": flower.get_hex_by_id(6)})

        hex_15 = flower.get_hex_by_id(15)
        hex_15.connections.append({"direction": "a", "hex": flower.get_hex_by_id(19)})
        hex_15.connections.append({"direction": "b", "hex": flower.get_hex_by_id(18)})
        hex_15.connections.append({"direction": "c", "hex": flower.get_hex_by_id(13)})
        hex_15.connections.append({"direction": "d", "hex": flower.get_hex_by_id(10)})
        hex_15.connections.append({"direction": "e", "hex": flower.get_hex_by_id(12)})
        hex_15.connections.append({"direction": "f", "hex": flower.get_hex_by_id(17)})

        hex_16 = flower.get_hex_by_id(16)
        hex_16.connections.append({"direction": "a", "hex": flower.get_hex_by_id(6)})
        hex_16.connections.append({"direction": "b", "hex": flower.get_hex_by_id(4)})
        hex_16.connections.append({"direction": "c", "hex": flower.get_hex_by_id(19)})
        hex_16.connections.append({"direction": "d", "hex": flower.get_hex_by_id(11)})
        hex_16.connections.append({"direction": "e", "hex": flower.get_hex_by_id(13)})
        hex_16.connections.append({"direction": "f", "hex": flower.get_hex_by_id(18)})

        hex_17 = flower.get_hex_by_id(17)
        hex_17.connections.append({"direction": "a", "hex": flower.get_hex_by_id(2)})
        hex_17.connections.append({"direction": "b", "hex": flower.get_hex_by_id(19)})
        hex_17.connections.append({"direction": "c", "hex": flower.get_hex_by_id(15)})
        hex_17.connections.append({"direction": "d", "hex": flower.get_hex_by_id(12)})
        hex_17.connections.append({"direction": "e", "hex": flower.get_hex_by_id(14)})
        hex_17.connections.append({"direction": "f", "hex": flower.get_hex_by_id(11)})

        hex_18 = flower.get_hex_by_id(18)
        hex_18.connections.append({"direction": "a", "hex": flower.get_hex_by_id(3)})
        hex_18.connections.append({"direction": "b", "hex": flower.get_hex_by_id(9)})
        hex_18.connections.append({"direction": "c", "hex": flower.get_hex_by_id(16)})
        hex_18.connections.append({"direction": "d", "hex": flower.get_hex_by_id(13)})
        hex_18.connections.append({"direction": "e", "hex": flower.get_hex_by_id(15)})
        hex_18.connections.append({"direction": "f", "hex": flower.get_hex_by_id(19)})

        hex_19 = flower.get_hex_by_id(19)
        hex_19.connections.append({"direction": "a", "hex": flower.get_hex_by_id(19)})
        hex_19.connections.append({"direction": "b", "hex": flower.get_hex_by_id(19)})
        hex_19.connections.append({"direction": "c", "hex": flower.get_hex_by_id(18)})
        hex_19.connections.append({"direction": "d", "hex": flower.get_hex_by_id(15)})
        hex_19.connections.append({"direction": "e", "hex": flower.get_hex_by_id(17)})
        hex_19.connections.append({"direction": "f", "hex": flower.get_hex_by_id(19)})

    
    def get_hex_by_id(self, id):
        got_hex = list(filter(lambda x: x.id == id, self.hexes))
        if len(got_hex) > 0:
            return got_hex[0]
        else:
            return None

# Some example hex flowers
class TerrainFlower(HexFlower):
    def __init__(self, name="terrain"):
        super().__init__(name)

        for h in self.hexes:
            if h.id in [1,2,3,5]:
                h.type = "plains"
            if h.id in [4,7]:
                h.type = "plains"
            if h.id in [6,8]:
                h.type = "plains"
            if h.id in [10]:
                h.type = "depression"
            if h.id in [9,12]:
                h.type = "hills"
            if h.id in [11,13]:
                h.type = "hills"
            if h.id in [14]:
                h.type = "hills"
            if h.id in [16]:
                h.type = "hills"
            if h.id in [15,17,18]:
                h.type = "foothills"
            if h.id in [19]:
                h.type = "mountains"
            
            # Specical disconnects
            if h.id == 14:
                h.delete_connection_by_direction("e")

            if h.id == 15:
                for d in ["c","d","e"]:
                    h.delete_connection_by_direction(d)

            if h.id == 16:
                h.delete_connection_by_direction("c")
            
            if h.id == 17:
                for d in ["a","d","e","f"]:
                    h.delete_connection_by_direction(d)

            if h.id == 18:
                for d in ["a","b","c","d"]:
                    h.delete_connection_by_direction(d)
