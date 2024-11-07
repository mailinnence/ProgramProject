<!DOCTYPE html>
<html>
<head>
    <title>파일 다운로드 예제</title>
    <style>
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>

<?php
if (isset($_GET['download']) && $_GET['download'] === '1') {
    $file = 'fake.exe'; // 다운로드할 파일의 경로 및 이름

    if (file_exists($file)) {
        header('Content-Description: File Transfer');
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="'.basename($file).'"');
        header('Expires: 0');
        header('Cache-Control: must-revalidate');
        header('Pragma: public');
        header('Content-Length: ' . filesize($file));
        ob_clean();
        flush();
        $fp = fopen($file, 'rb');
        while (!feof($fp)) {
            echo fread($fp, 1024);
        }
        fclose($fp);
        exit;
    } else {
        echo '파일을 찾을 수 없습니다.';
    }
}
?>




<body>
    <form name="form1" method="get">
        <button type="submit" name="download" value="1">
            <img src="py.PNG" alt="이미지">
        </button>
    </form>
</body>
</html>
