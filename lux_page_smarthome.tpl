<!DOCTYPE html>
<html>
<head>
<title>Lux-Messungen</title>
</head>
<body>
<h1>Lux-Messungen</h1>
<a class="button" href=/get_csv> <button>Export als .CSV</button></a>
<a class="button" href=/get_json> <button>Export als .JSON</button></a>
<br>
<br>
<table border=1>
<tr><th>Helligkeit(in Lux)</th><th>Datum</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    </tr>
%end
</table>
</body>
</html>