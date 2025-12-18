<?php
// Simulazione carico di lavoro (sleep)
usleep(100000+rand(-100000/5, 100000/5));
?>
<!DOCTYPE html>
<html>
<head><title>Servizio: news.php</title></head>
<body>
    <h1>Modulo Dinamico: news.php</h1>
    <p>Elaborazione completata.</p>
    <p>Tempo di esecuzione simulato: 100 ms</p>
    <p>Richiesta processata dal server: <?php echo $_SERVER['SERVER_ADDR']; ?></p>
</body>
</html>
