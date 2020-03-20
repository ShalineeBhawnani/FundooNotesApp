import { Component, OnInit } from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import {MatDialog, MatDialogRef,MAT_DIALOG_DATA,MatDialogConfig} from '@angular/material/dialog';
import { NoteDialogComponent } from '../note-dialog/note-dialog.component';
import { SharedService } from '../../services/shared.service';

export interface DialogData {
  // title: string;
  // note: string;
  }
@Component({

  selector: 'app-displaynotes',
  templateUrl: './displaynotes.component.html',
  styleUrls: ['./displaynotes.component.scss'],
  providers: [UserService]
})

export class DisplaynotesComponent implements OnInit {

fileNameDialogRef: MatDialogRef<NoteDialogComponent>;

  notes = [
    {   title: ' ',
        note: ' '}
      ]

  constructor(private userSerive: UserService,public dialog:MatDialog,
    private sharedService: SharedService) {

    this.getNotes();

   }

  ngOnInit(){


  }

   getNotes=()=>{

      this.userSerive.getAllNote().subscribe(
        data => {
          this.notes = data;
        },
        error => {
          console.log(error);
        }
      );
    }
    openDialog(note) {
      {
      this.fileNameDialogRef = this.dialog.open(NoteDialogComponent, {
      hasBackdrop: false,
      data: note
      });
      }
      }


}




