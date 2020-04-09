import sys,csv,json  

if(len(sys.argv) - 1 <= 0):
    print("Usage: convert_csv_to_json.py filename.csv filename.json")
    exit()
f = open(sys.argv[1], 'rU' )  
reader = csv.DictReader( f, fieldnames = ( "value","descr" ))  
#out = json.dumps( [ row for row in reader ] )  
out = json.dumps( [ row for row in reader ], indent=4) 
f = open(sys.argv[2], 'w')  
f.write(out)  
print("Done");