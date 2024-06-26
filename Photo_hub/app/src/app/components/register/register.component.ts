import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router'

import { Registration } from '../../models/registration';

import { AuthenticationService } from '../../services/authentication.service'
import { NotificationService } from '../../services/notification.service';

@Component({
    selector: 'register',
    templateUrl: 'static/app/components/register/register.component.html',
})
export class RegisterComponent implements OnInit {
    private _newUser: Registration;

    constructor(public authenticationService: AuthenticationService,
                public notificationService: NotificationService,
                public router: Router) { }

    ngOnInit() {
        this._newUser = new Registration('', '', '', '');
    }

    register(): void {
        this.authenticationService.register(this._newUser.Username, this._newUser.Email, this._newUser.Password)
            .subscribe(data => {
                this.notificationService.printSuccessMessage('Dear ' + this._newUser.Username + ', your account created, Enjoy!');
                this.router.navigate(['/']);
            },
            error =>
            {
                this.notificationService.printErrorMessage(error);
            });
    };
}
