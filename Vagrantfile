Vagrant.configure("2") do |config|
    config.vm.define :minerador do |minerador|
        minerador.vm.box = "ubuntu/bionic64"
        minerador.vm.network "private_network", ip: "192.168.1.10"
        minerador.vm.provision "ansible_local" do |ansible|
            ansible.playbook = "ansible/docker.yml"
        end
        minerador.vm.provider "virtualbox" do |minerador_provider|
            minerador_provider.memory = 512
        end
    end
end