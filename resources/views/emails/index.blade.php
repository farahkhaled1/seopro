{{-- 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>SEOPro</title>
</head>
<body>
    <h1>SEOPro </h1>
    <h3>{{$data['body']}}</h3>
    
</body>
</html> --}}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>SEOPro</title>
</head>
<body>
    <h1>SEOPro</h1>
    <h3>{!! nl2br(e($data['body'])) !!}</h3>
</body>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
    }

    h1 {
        color: #333333;
        margin-top: 0;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        margin-bottom: 10px;
    }
</style>
</html>
