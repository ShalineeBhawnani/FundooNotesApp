import { Component, OnInit } from '@angular/core';

import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { HttpClient, HttpResponse ,HttpHeaders} from '@angular/common/http';


@Component({
  selector: 'app-notes',
  templateUrl: './notes.component.html',
  styleUrls: ['./notes.component.scss'],
  providers:[AuthenticationService,UserService]

})
export class NotesComponent implements OnInit {
  createnote: FormGroup;
  loading = false;
  submitted = false;

    constructor(
       private formBuilder: FormBuilder,
       private router: Router,
       private userService: UserService,
       private alertService: AlertService) { }

    ngOnInit() {

       this.createnote = this.formBuilder.group({

        title: [''],
        note: [''],
        // label_note: [''],
        // add_picture: [''],
        // is_archived: [''],
        // is_bin: [''],
        // color: [''],
        // more: [''],
        // reminder: [''],
        // collaborators: [''],


       });
   }

   // convenience getter for easy access to form fields
   get f() { return this.createnote.controls; }

   notesUser() {
    this.submitted = true;
    // let user_id=JSON.parse(localStorage.getItem('user'));

    // stop here if form is invalid
    if (this.createnote.invalid) {
        return;
    }
      // let noteData = {

      //   // user : this.user_id,

      //   title :this.createnote.value,
      //   note :this.createnote.value,
      //   // label_note :this.registerForm.value,


      // }

       this.loading = true;
       this.userService.note(this.createnote.value)
           .subscribe(
               data => {
                   this.alertService.success('notes created successfully', true);
                   // this.router.navigate(['/label']);
               },
               error => {
                   this.alertService.error(error);
                   this.loading = false;
               });
   }
}
