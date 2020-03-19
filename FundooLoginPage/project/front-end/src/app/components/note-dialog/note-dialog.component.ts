import { Component, OnInit ,Inject} from '@angular/core';
import {MatDialog, MatDialogRef,MAT_DIALOG_DATA} from '@angular/material/dialog';

@Component({
  selector: 'app-note-dialog',
  templateUrl: './note-dialog.component.html',
  styleUrls: ['./note-dialog.component.scss']
})
export class NoteDialogComponent implements OnInit {
  title: string;
  note: string;

constructor( private dialogRef: MatDialogRef<NoteDialogComponent>,
  @Inject(MAT_DIALOG_DATA) public data: any) {
  console.log("fbdjfbdjfbdjfb: ", this.data);
  }

  ngOnInit() {
  }

  onNoClick(): void {
  this.dialogRef.close();
  }

  }




