import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
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
  label:FormControl=new FormControl('');
  labels:any;
  editLabel:boolean=true;
  editedTextLabel=new FormControl('');

  // loading = false;
  // submitted = false;

    constructor(
      private userService: UserService,
      private alertService: AlertService,) { }

    ngOnInit() {

     
    }

    // convenience getter for easy access to form fields
    createLabel()

    {
      console.log(this.label.value);
       let noteData = {

             lable : this.label.value

    }

      this.userService.label(noteData)

    .subscribe(
        (data) => {
            console.log('label: ' + noteData);
            console.log(noteData.lable);
            this.alertService.success('label created successfully', true);
            // this.router.navigate(['/label']);
        },
        error => {
            this.alertService.error(error);

        });
  }

    }
