$(document).ready(function() {
    $('#sap').DataTable( {
        "ajax": {
            "url": "/api/sap/data_tables",
            "dataSrc": "data"
        }
    });
});