<title>Lux-Messungen</title>
<h1>Lux-Messungen</h1>



<a href="/csv/output.csv" download>.csv</a>

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
