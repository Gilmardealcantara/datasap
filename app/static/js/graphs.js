// Discussion groups- how many times the student participate on discussion groups (numeric:0-100)'
$.get("/api/sap/graph/2", function( data ) {

var visualization = d3plus.viz()
    .container("#viz")
    .data(data.data)
    .type("bar")
    .id("topic")
    .x("topic")
    .y("discussion")
    .ui([{
        "method" : "y",
        "value"  : ["discussion", "raisedhands", "visitedresources", "announcementsview"]
    }])
    .title('Media da Participação dos alunos nos grupos de discurção por curso.')
    .draw()

});
