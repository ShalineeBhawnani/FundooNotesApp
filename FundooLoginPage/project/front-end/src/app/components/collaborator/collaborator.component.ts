import { Component, OnInit, Output, EventEmitter, Inject } from '@angular/core';
import { MatDialogRef,MatSnackBar,MatDialog, MAT_DIALOG_DATA } from '@angular/material';
import { UserService } from '../../services/user.service';


@Component({
  selector: 'app-collaborator',
  templateUrl: './collaborator.component.html',
  styleUrls: ['./collaborator.component.scss']
})
export class CollaboratorComponent implements OnInit {
  allUsers
  email:string;
  note_id:any;
  collab_users:any;

  constructor(public dialogRef: MatDialogRef<CollaboratorComponent>,
    @Inject(MAT_DIALOG_DATA) public data, public userService: UserService,
    private snackBar:MatSnackBar) { }

    ngOnInit() {
      this.userService.get_all_collab_users(this.data).subscribe(
        data1 => {
    
        this.collab_users = data1;
        console.log("received collab users",data1)
        },
        
        error => {
        console.log(error);
        }
        );
      
    }
  
    add_new_collaborators(email:string)
    {
      let emaildata = {
        email: email,
      }
      console.log(emaildata)
  
      this.userService.addcollaborators(emaildata,this.data).subscribe(
        (data1) => {
          this.snackBar.open(data1.toString(),'',{
            duration:3000,
            verticalPosition:'bottom'
          });
       
        },
        
        error => {
          alert('update failed')
        
        });
     
     
    }
    close(){
      this.dialogRef.close();
    }
  
  
}