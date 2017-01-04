// Discussion groups- how many times the student participate on discussion groups (numeric:0-100)'
$.get("/api/sap/graph/2", function( data ) {

var visualization = d3plus.viz()
    .container("#bar")
    .data(data.data)
    .type("bar")
    .id("topic")
    .x("topic")
    .y("discussion")
    .ui([{
        "method" : "y",
        "value"  : ["discussion", "raisedhands", "visitedresources", "announcementsview"]
    }])
    .draw()


var visualization = d3plus.viz()
    .container("#treemap")
    .data(data.data)
    .type("tree_map")
    .id("topic")
    .x("topic")
    .size("discussion")
    .ui([{
        "method" : "size",
        "value"  : ["discussion", "raisedhands", "visitedresources", "announcementsview"]
    }])
    .draw()

var visualization = d3plus.viz()
    .container("#bubbles")
    .data(data.data)
    .type("bubbles")
    .id("topic")
    .x("topic")
    .size("discussion")
    .ui([{
        "method" : "size",
        "value"  : ["discussion", "raisedhands", "visitedresources", "announcementsview"]
    }])
    .draw()

});
