import convertapi

convertapi.api_secret = '니 api 키 집어넣어야함'
convertapi.convert('pdf', {
    'File': 'C:\convert\sample.ppt'
}, from_format = 'ppt').save_files('C:\convert\out')