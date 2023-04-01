import convertapi

convertapi.api_secret = 'input your api key'
convertapi.convert('pdf', {
    'File': 'C:\convert\sample.ppt'
}, from_format = 'ppt').save_files('C:\convert\out')