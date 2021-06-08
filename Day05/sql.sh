#!/bin/sh

function kill_db() {
    echo "kill postgresql"
    brew services stop postgresql
    case $1 in
    "s" | "l" | "show" | "list")
        brew services list
        ;;
    esac

}

function run_db() {
    pg_ctl -D djangotraining start
    case $1 in
    "")
        echo "starting DB"
    	brew services start postgresql
        ;;
    "re")
        echo "restarting DB"
		brew services restart postgresql
        ;;
    esac
    psql postgres
}

case $1 in
"" | run | runsql)
    run_db
    ;;
l | log | login)
    u="djangouser"
    echo "login as $u"
    psql postgres -U $u
    ;;
k | kill)
    kill_db $2 # s / show / l / list 로 현재 서비스 리스트 표시
    ;;
r | re | rerun | restart)
    run_db re
    ;;
*)
    echo "input ->$1 not found in available parameters"
    ;;
esac
