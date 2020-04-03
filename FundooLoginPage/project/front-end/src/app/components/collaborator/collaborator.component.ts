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
  constructor(public dialogRef: MatDialogRef<CollaboratorComponent>,
    @Inject(MAT_DIALOG_DATA) public data, public userService: UserService) { }

  ngOnInit() {
    this.userService.allRegisterdUsers().subscribe((response) => {
      this.allUsers = response
      console.log(this.allUsers)
      });
  }
}