$(document).ready(function() {
    var headers = {
         0 : "id", 
         1 : "gender", 
         2 : "NationalITy", 
         3 : "PlaceofBirth", 
         4 : "StageID", 
         5 : "GradeID", 
         6 : "SectionID", 
         7 : "Topic", 
         8 : "Semester", 
         9 : "Relation", 
         10 : "raisedhands", 
         11 : "VisITedResources", 
         12 : "AnnouncementsView", 
         13 : "Discussion", 
         14 : "ParentschoolSatisfaction", 
         15 : "StudentAbsenceDays", 
         16 : "Class"
    }


    $('#sap').DataTable( {
        "ajax": {
            "url": "/api/sap/data_tables",
            "dataSrc": "data",
        },
        "scrollX": true,
        responsive: true,
        "columns": [    
            {
                render: function(data, type, row, meta){
                    return row[headers['0']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['1']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['2']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['3']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['4']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['5']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['6']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['7']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['8']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['9']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['10']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['11']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['12']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['13']]
                }
            },                
            {
                render: function(data, type, row, meta){
                    return row[headers['14']]
                }
            },
            {
                render: function(data, type, row, meta){
                    return row[headers['15']]
                }
            },
            {
                render: function(data, type, row, meta){
                    return row[headers['16']]
                }
            }
        ],
        "fnRowCallback": function( nRow, aData, iDisplayIndex, iDisplayIndexFull ) {
            if ( iDisplayIndex%2 == 0 )
            {
                $('td', nRow).css('background-color', '#f6dd89');
            }
            else
            {
                $('td', nRow).css('background-color', '#fff');
            }
        }, 
        initComplete: function () {
            
        }
    });
});
