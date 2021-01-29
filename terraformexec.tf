resource "null_resource" "example" {
  
   
 provisioner "file" {
    source      = "/Users/Sandeep.Gopi/Documents/python_check/Hello_World_Sample_App.py"
    destination = "/Users/Sandeep.Gopi/Hello-World-App-Test/Hello_World_Sample_App.py"
   
  
  }

}


