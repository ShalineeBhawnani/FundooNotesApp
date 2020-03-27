import { Component, OnInit, Output, EventEmitter, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-collaborator',
  templateUrl: './collaborator.component.html',
  styleUrls: ['./collaborator.component.scss']
})
export class CollaboratorComponent implements OnInit {
  name: string;
  email: string;
  searchResultList;
  collaborator;
  collaborators: any[];
  collaboratorBody;
  constructor(public dialogRef: MatDialogRef<CollaboratorComponent>,
    @Inject(MAT_DIALOG_DATA) public data, public noteService: UserService) { }

  ngOnInit() {
    this.data=this.data.note;
    this.name = localStorage.getItem('firstName');
    this.email = localStorage.getItem('email');
    console.log(this.data)
    this.collaborators = this.data.collaborators
    if (this.data['id'] == undefined) {
      if (this.data['collaborators'] == undefined) {
        this.collaborators = [];
      }
    }
  }

  // searchlist(data) {
    
  //   //console.log("inside searching",data)
  //   if (data != '') {
  //     this.noteService.searchUserList(
  //       { "searchWord": data }).subscribe(data => {
  //         //console.log(data)
  //         this.searchResultList = data['data']['details'];
  //       })
  //   }
  // }
  addCollaborator() {
    
    try {
      if (this.email != this.collaboratorBody.email && this.collaboratorBody.email != '') {

        if (this.data['id'] == undefined) {
          this.collaborators.push(this.collaboratorBody);
          this.collaborator = "";
          console.log("Collaborators",this.collaborators)
        }
        else {
          this.noteService.addCollaborator().subscribe(result => {
            this.collaborators.push(this.collaboratorBody);
            this.collaborator = "";
            // this.snackbar.open("Collaborator added successfully")
            
          })
        }
      }
    } catch (error) {
      console.log("inside addCollab",error)
      // this.snackbar.open("Error during adding collaborator",'Retry');
    }
  }
  setCollaborator(userDetails) {
    console.log(userDetails)
    if (this.email !== userDetails.email && userDetails.email != '') {
      this.collaborator = userDetails.email;
      console.log(userDetails);
      this.collaboratorBody = {
        "firstName": userDetails.firstName,
        "lastName": userDetails.lastName,
        "email": userDetails.email,
        "userId": userDetails.userId
      }
    }
  }
  // removeCollaborator(collaboratorId) {
  //   if (this.data['id'] !== undefined) {
  //     this.noteService.removeCollaborator(this.data['id'], collaboratorId).subscribe(result => {
  //       this.snackbar.open('Collaborator removed successfully')
  //     },
  //     error=>{
  //       this.snackbar.open('Error in removing Collaborator', 'Retry')
  //     })
  //   }
  //   var count = 0;
  //   this.collaborators.forEach(collaborator => {
  //     if (collaborator.userId == collaboratorId) {
  //       this.collaborators.splice(count, 1);
  //     }
  //     else
  //       count++;
  //   });
  //   return;
  // }
  cancel() {
    this.dialogRef.close();
  }

}
