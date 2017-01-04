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
    .title('The average participation rate of students in discursions, raises Hand in Classroon,  visits a course content and views new announcements')
    .draw()


var visualization = d3plus.viz()
    .container("#treemap")
    .data(data.data)
    .type("treemap")
    .id("topic")
    .x("topic")
    .size("discussion")
    .ui([{
        "method" : "size",
        "value"  : ["discussion", "raisedhands", "visitedresources", "announcementsview"]
    }])
    .title('The average participation rate of students in discursions, raises Hand in Classroon,  visits a course content and views new announcements')
    .draw()



});
