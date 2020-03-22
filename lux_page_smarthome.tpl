<title>Lux-Messungen</title>
<h1>Lux-Messungen</h1>



<a href="output.csv" download>.csv</a>
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
