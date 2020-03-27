import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from '@angular/forms';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { HttpClient, HttpResponse ,HttpHeaders} from '@angular/common/http';


@Component({
  selector: 'app-label',
  templateUrl: './label.component.html',
  styleUrls: ['./label.component.scss'],
  providers:[AuthenticationService],

})
export class LabelComponent implements OnInit {
  labels = [
    {   
        label: ' ',
    }
      ]
constructor(private userService: UserService) {
    
      }

ngOnInit() {
  this.getLabels();

}
getLabels=()=>{
  console.log("called when note added ")
  this.userService.getAllLabel().subscribe(
    data => {
      console.log("my data",data)
      this.labels = data;
    },
    
    error => {
      console.log(error);
    }
  );
}
}