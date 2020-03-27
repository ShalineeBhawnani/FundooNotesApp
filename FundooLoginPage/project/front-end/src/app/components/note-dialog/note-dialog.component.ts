import { Component, OnInit ,Inject} from '@angular/core';
import { MatDialogRef,MAT_DIALOG_DATA} from '@angular/material/dialog';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';


@Component({
  selector: 'app-note-dialog',
  templateUrl: './note-dialog.component.html',
  styleUrls: ['./note-dialog.component.scss']
})
export class NoteDialogComponent implements OnInit {
  title: string;
  note: string;

constructor( private dialogRef: MatDialogRef<NoteDialogComponent>,
  @Inject(MAT_DIALOG_DATA) public data: any,
  private userService: UserService,
  private alertService:AlertService) {
  console.log("this data: ", this.data);
  }

  ngOnInit() {

  }

  updateClick(title:string,note:string): void {
    let notedata = {
      title: title,
      note: note,

      }
      this.userService.updateNotes(notedata,this.data.id)
      .subscribe(
          (data) => {
              this.alertService.success('notes updated successfully', true);
              
          },
          error => {
              this.alertService.error(error);

          });
          this.dialogRef.close(notedata);
    }

      }


